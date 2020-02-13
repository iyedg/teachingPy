from typing import Any, List

import attr
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
from sympy import Eq, lambdify, solve, sympify


@attr.s()
class Constraint:
    lhs: str = attr.ib()
    x_range: np.array = attr.ib()
    rhs: str = attr.ib(default="0")
    label: str = attr.ib(default="")
    transformation: Any = attr.ib(default=None)
    # transformation: Any = None  # TODO: check for correct type

    # property
    def evaluate(self):
        s_lhs = sympify(self.lhs)
        s_rhs = sympify(self.rhs)
        n_symbols = len(s_lhs.free_symbols.union(s_rhs.free_symbols))

        logger.debug(f"{s_lhs} = {s_rhs} has {n_symbols} symbols")

        if self.rhs == "0":
            logger.debug(f"{s_lhs} has {len(s_lhs.free_symbols)}")
            return lambdify("x", self.lhs)(self.x_range)
        elif self.transformation:
            # TODO: use y when x is not in args
            return lambdify("x", self.transformation.lhs)(self.x_range)
        else:
            # Needs to be smarter about x = a and y = b forms
            try:
                new_lhs = solve(Eq(s_lhs, s_rhs), "y")[0]
            except IndexError as e:
                logger.error(e)
                # TODO: check for the presence of two variables to prevent this
                return (
                    self.x_range
                )  # TODO: remove !!! used just to avoid problems downstream
            self.transformation = Constraint(lhs=new_lhs, rhs=0, x_range=self.x_range)
            return self.evaluate()


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

    def plot_constraint(self, constraint, ax=None, *args, **kwargs):
        ax = ax or plt.gca()
        ax.plot(
            constraint.x_range,
            constraint.evaluate(),
            label=constraint.label,
            *args,
            **kwargs,
        )

    def plot_constraints(self, ax=None, *args, **kwargs):
        ax = ax or plt.gca()
        for constraint in self.constraints:
            self.plot_constraint(constraint, ax, *args, **kwargs)
        plt.grid(True)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        plt.legend()
