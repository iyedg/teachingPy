from typing import Any, List
from itertools import combinations

import attr
import matplotlib.pyplot as plt
import numpy as np
import sympy
from loguru import logger
from sympy import Eq, lambdify, solve, sympify
from sympy.abc import x, y


# Courtesy of https://github.com/sympy/sympy/issues/5642#issuecomment-516419510
# Handles cases when solution is a constant function
def broadcast(fun):
    return lambda *x: np.broadcast_arrays(fun(*x), *x)[0]


@attr.s()
class Constraint:
    lhs: str = attr.ib()
    rhs: str = attr.ib(default="0")
    label: str = attr.ib(default="")
    operator: str = attr.ib(default="<=")

    def __attrs_post_init__(self):
        self._free_symbols: int = None
        self._func = None
        self._s_lhs = sympify(self.lhs)
        self._s_rhs = sympify(self.rhs)
        self.lhs = self._s_lhs
        self.rhs = self._s_rhs

    @property
    def func(self):
        if not self._func:
            # TODO: validate on init
            assert (x in self.free_symbols) or (y in self.free_symbols)
            assert 0 < len(self.free_symbols) <= 2

            # Solving lhs = rhs
            e = Eq(self._s_lhs, self._s_rhs)

            # TODO: an edge case is x = x which returns a boolean

            # Chcking for y first to avoid checking
            # for the number of args. If y is in args,
            # we solve for y regardless of whether
            # there is an x or not
            if y in self.free_symbols:
                solutions = solve(e, y)
            else:
                solutions = solve(e, x)

            if len(solutions) < 1:
                raise Exception(f"No solutions found for {self.lhs} = {self.rhs}")
            elif len(solutions) > 1:
                raise Exception(
                    f"Too many solutions found for {self.lhs} = {self.rhs}, constraints must be linear"
                )

            solution = solutions[0]
            if y in self.free_symbols:
                self._func = broadcast(lambdify(x, solution, "numpy"))
            else:
                self._func = broadcast(lambdify(y, solution, "numpy"))
        return self._func

    @property
    def free_symbols(self):
        if not self._free_symbols:
            s_lhs = sympify(self.lhs)
            s_rhs = sympify(self.rhs)
            self._free_symbols = s_lhs.free_symbols.union(s_rhs.free_symbols)
        return self._free_symbols


@attr.s()
class GraphicalProblem:
    # TODO: accept only linear constraints
    constraints: List = attr.ib(default=[])

    def add_constraints(self, *constraints, clear=True):
        # TODO: add another method to extend constraints list
        if clear:
            self.constraints = constraints
        else:
            self.constraints.extend(constraints)

    def plot_constraint(self, constraint, _range, ax=None, *args, **kwargs):
        ax = ax or plt.gca()
        if (len(constraint.free_symbols) == 1) and (x in constraint.free_symbols):
            x_range = constraint.func(_range)
            y_range = _range
        else:
            y_range = constraint.func(_range)
            x_range = _range

        ax.plot(
            x_range, y_range, label=constraint.label, *args, **kwargs,
        )

    def plot_constraints(self, _range, ax=None, *args, **kwargs):
        ax = ax or plt.gca()
        for constraint in self.constraints:
            self.plot_constraint(constraint, _range, ax, *args, **kwargs)
        plt.grid(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.legend()

    def intersection_points(self):
        intersections = []
        for constraint1, constraint2 in combinations(self.constraints, 2):
            e1 = Eq(constraint1.lhs, constraint1.rhs)
            e2 = Eq(constraint2.lhs, constraint2.rhs)
            intersection = sympy.linsolve([e1, e2], [x, y])
            if intersection != sympy.EmptySet:
                intersections.append(intersection)
            else:
                logger.warning(f"{e1} and {e2} have no intersections")
        return intersections
