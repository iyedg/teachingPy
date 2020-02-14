# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.3
#   kernelspec:
#     display_name: teachingpy
#     language: python
#     name: teachingpy
# ---

# + Collapsed="false" persistent_id="7faa24a2-9c6b-4b9b-96b3-000fc621f83a" last_executed_text="%reload_ext autoreload\n%autoreload 2" execution_event_id="f495b5a0-fdb0-465e-b875-287dfa36275d"
# %reload_ext autoreload
# %autoreload 2

# + Collapsed="false" execution_event_id="ecc30802-76c0-452d-a49a-52b4be7a06b4" last_executed_text="import matplotlib as mpl\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport numpy as np\nfrom sympy.abc import x, y\nfrom sympy import Eq, lambdify, solve, sympify, symbols\n\nfrom palettable.tableau import BlueRed_12\nfrom teachingpy.operations_research.graphical import Constraint, GraphicalProblem\nfrom IPython.display import display\n\nmpl.rc(\"text\", usetex=True)\n# mpl.rcParams[\"axes.prop_cycle\"] = mpl.cycler(color=BlueRed_12.mpl_colors)" persistent_id="27d4caf3-2082-4138-8789-b13da81f93e5"
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sympy.abc import x, y
from sympy import Eq, lambdify, solve, sympify, symbols

from palettable.tableau import BlueRed_12
from teachingpy.operations_research.graphical import Constraint, GraphicalProblem
from IPython.display import display

mpl.rc("text", usetex=True)
# mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=BlueRed_12.mpl_colors)

# + [markdown] Collapsed="false" persistent_id="441b062d-a292-46d1-84f7-1dc3042b6279"
# $$y=mx+b$$
# $$y=m(x-x_0)+(b+y_0)$$

# + [markdown] Collapsed="false" persistent_id="0ae77ed8-2633-4fad-8123-eb24f756f365"
# http://www.geom.uiuc.edu/docs/reference/CRC-formulas/node9.html

# + persistent_id="64fa0802-334d-4a5c-b9de-52ee218ca75f" last_executed_text="sns.set_style(\"whitegrid\")" execution_event_id="2b612ac6-e1c0-4519-989e-4d7dc14e3f5a" Collapsed="false"
sns.set_style("whitegrid")

# + Collapsed="false" execution_event_id="435eb8b8-50b8-44a6-bc90-e90cdd71158c" last_executed_text="# aspect_ratio = 16 / 9\naspect_ratio = 1\nw = 8\nh = w / aspect_ratio\nfig, ax = plt.subplots(figsize=(w, h))\n\ntvs_radios_problem = GraphicalProblem()\n\n_range = np.arange(0, 10)\n\nc1 = Constraint(\n    lhs=\"6 * x + 4 * y\", rhs=\"24\", label=\"Labor constraint:\\n$6x + 4y \\leq 24$\"\n)\nc2 = Constraint(lhs=\"x + 2 * y\", rhs=\"6\", label=\"c2: $x + 2y \\leq 6$\")\nc3 = Constraint(lhs=\"y - x\", rhs=\"1\", label=\"c3: $y - x \\leq 1$\")\nc4 = Constraint(lhs=\"x\", rhs=\"2\", label=\"c4: $x = 2$\")\n\nc5 = Constraint(lhs=\"y\", rhs=\"0\", label=\"c6: $y > 0$\")\nc6 = Constraint(lhs=\"x\", rhs=\"0\", label=\"c7: $x > 0$\")\n\ntvs_radios_problem.add_constraints(c1, c2, c3, c4, c5, c6)\ntvs_radios_problem.plot_constraints(_range=np.arange(0, 10), lw=3)\n\n\nplt.xlim(0, 5)\nplt.ylim(0, 5)\nax.set_title(\"Three-constraint problem\")\nplt.grid(True)\nplt.tight_layout()" persistent_id="8d85ef9f-118e-4e6f-bc88-032f55fe1329"
# aspect_ratio = 16 / 9
aspect_ratio = 1
w = 8
h = w / aspect_ratio
fig, ax = plt.subplots(figsize=(w, h))

tvs_radios_problem = GraphicalProblem()

_range = np.arange(0, 10)

c1 = Constraint(
    lhs="6 * x + 4 * y", rhs="24", label="Labor constraint:\n$6x + 4y \leq 24$"
)
c2 = Constraint(lhs="x + 2 * y", rhs="6", label="c2: $x + 2y \leq 6$")
c3 = Constraint(lhs="y - x", rhs="1", label="c3: $y - x \leq 1$")
c4 = Constraint(lhs="x", rhs="2", label="c4: $x = 2$")

c5 = Constraint(lhs="y", rhs="0", label="c6: $y > 0$")
c6 = Constraint(lhs="x", rhs="0", label="c7: $x > 0$")

tvs_radios_problem.add_constraints(c1, c2, c3, c4, c5, c6)
tvs_radios_problem.plot_constraints(_range=np.arange(0, 10), lw=3)


plt.xlim(0, 5)
plt.ylim(0, 5)
ax.set_title("Three-constraint problem")
plt.grid(True)
plt.tight_layout()

# + Collapsed="false" persistent_id="6166a0f7-fd35-415d-a004-da91a2b59491" last_executed_text="tvs_radios_problem.intersection_points()" execution_event_id="a310dadb-9572-4782-a664-fabd2e088456"
tvs_radios_problem.intersection_points()

# + Collapsed="false" persistent_id="89d79e05-53e9-49d0-bdfc-308e821368f7" last_executed_text="test_prob = GraphicalProblem()\nc1 = Constraint(lhs=\"x\", rhs=\"4\", label=\"$x \\leq 4$\")\nc2 = Constraint(lhs=\"8 * x - 4 * y\", rhs=\"1\", label=\"$8 x - 4 y \\leq 1$\")\nc3 = Constraint(lhs=\"2 * x + 3 * y\", rhs=\"12\", label=\"$2 x + 3 y \\leq 12$\")\ntest_prob.add_constraints(c1, c2, c3)" execution_event_id="eacff0ed-19ee-415f-9ec2-600c5894ebd4"
test_prob = GraphicalProblem()
c1 = Constraint(lhs="x", rhs="4", label="$x \leq 4$")
c2 = Constraint(lhs="8 * x - 4 * y", rhs="1", label="$8 x - 4 y \leq 1$")
c3 = Constraint(lhs="2 * x + 3 * y", rhs="12", label="$2 x + 3 y \leq 12$")
test_prob.add_constraints(c1, c2, c3)


# + persistent_id="377306c5-9c8f-4635-997c-730072f53ecc" Collapsed="false" last_executed_text="aspect_ratio = 1\nw = 10\nh = w / aspect_ratio\nfig, ax = plt.subplots(figsize=(w, h))\ntest_prob.plot_constraints(_range=np.arange(0, 10))\nax.spines[\"bottom\"].set_position(\"zero\")\nax.spines[\"left\"].set_position(\"zero\")\nplt.ylim(0, 5)\nplt.xlim(0, 7)\nplt.grid(True)" execution_event_id="1a7b5461-9065-4117-aef7-4981944992af"
aspect_ratio = 1
w = 10
h = w / aspect_ratio
fig, ax = plt.subplots(figsize=(w, h))
test_prob.plot_constraints(_range=np.arange(0, 10))
ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")
plt.ylim(0, 5)
plt.xlim(0, 7)
plt.grid(True)

# + Collapsed="false" persistent_id="60e63b5c-2b79-4bd9-a2ca-627791aca698" last_executed_text="test_prob = GraphicalProblem()\nc1 = Constraint(lhs=\"6 * x + 4 * y\", rhs=\"24\", label=\"$c_1: 6  x + 4 y \\leq 24$\")\nc2 = Constraint(lhs=\"x + 2 * y\", rhs=\"6\", label=\"$c_2:x + 2y \\leq 6 $\")\nc3 = Constraint(lhs=\"y - x\", rhs=\"1\", label=\"\")\nc4 = Constraint(lhs=\"y\", rhs=\"2\", label=\"\")\nc5 = Constraint(lhs=\"y\", rhs=\"0\", label=\"$y=0$\")\nc6 = Constraint(lhs=\"x\", rhs=\"0\", label=\"$x=0$\")\ntest_prob.add_constraints(c1, c2, c3, c4, c5, c6)" execution_event_id="a204692e-5198-48c2-99ba-1760899d18a3"
test_prob = GraphicalProblem()
c1 = Constraint(lhs="6 * x + 4 * y", rhs="24", label="$c_1: 6  x + 4 y \leq 24$")
c2 = Constraint(lhs="x + 2 * y", rhs="6", label="$c_2:x + 2y \leq 6 $")
c3 = Constraint(lhs="y - x", rhs="1", label="")
c4 = Constraint(lhs="y", rhs="2", label="")
c5 = Constraint(lhs="y", rhs="0", label="$y=0$")
c6 = Constraint(lhs="x", rhs="0", label="$x=0$")
test_prob.add_constraints(c1, c2, c3, c4, c5, c6)

# + persistent_id="873406f3-3e1e-431d-92e7-3617b0bc2806" last_executed_text="c1_ineq = lambdify((x, y), c1.lhs <= c1.rhs)\nc2_ineq = lambdify((x, y), c2.lhs <= c2.rhs)" execution_event_id="3283ecca-ff38-4444-8841-4889d0e4a0bb" Collapsed="false"
c1_ineq = lambdify((x, y), c1.lhs <= c1.rhs)
c2_ineq = lambdify((x, y), c2.lhs <= c2.rhs)

# + Collapsed="false" persistent_id="fcba1f27-befc-4212-be64-db5b88d004ad" last_executed_text="aspect_ratio = 1\nw = 10\nh = w / aspect_ratio\n_range = np.arange(0, 10, 0.1)\nfig, ax = plt.subplots(figsize=(w, h))\ntest_prob.plot_constraints(_range=_range, lw=3)\n\nax.spines[\"bottom\"].set_position(\"zero\")\nax.spines[\"left\"].set_position(\"zero\")\nax.spines[\"left\"].set_visible(False)\nax.spines[\"bottom\"].set_visible(False)\n\nplt.ylim(0, 5)\nplt.xlim(0, 6)\nplt.grid(False)\n\nplt.annotate(\"$(2, 3)$\", (2, 3), textcoords=\"offset points\", xytext=(10, 0), ha=\"left\")\nplt.annotate(\n    \"$(8/3, 2)$\", (8 / 3, 2), textcoords=\"offset points\", xytext=(10, 10), ha=\"left\"\n)\n_range = np.arange(0, 100, 0.5)\nplt.fill_between(\n    _range,\n    c1.func(_range),\n    c4.func(_range),\n    where=(lambdify((x, y), c1.lhs)(_range, _range))\n    & (lambdify((x, y), c4.lhs)(_range, _range) ),\n)" execution_event_id="ffb916ef-75c3-463e-90fa-ea6541f5a6c1"
aspect_ratio = 1
w = 10
h = w / aspect_ratio
_range = np.arange(0, 10, 0.1)
fig, ax = plt.subplots(figsize=(w, h))
test_prob.plot_constraints(_range=_range, lw=3)

ax.spines["bottom"].set_position("zero")
ax.spines["left"].set_position("zero")
ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)

plt.ylim(0, 5)
plt.xlim(0, 6)
plt.grid(False)

plt.annotate("$(2, 3)$", (2, 3), textcoords="offset points", xytext=(10, 0), ha="left")
plt.annotate(
    "$(8/3, 2)$", (8 / 3, 2), textcoords="offset points", xytext=(10, 10), ha="left"
)
_range = np.arange(0, 100, 0.5)
plt.fill_between(
    _range,
    c1.func(_range),
    c4.func(_range),
    where=(lambdify((x, y), c1.lhs)(_range, _range))
    & (lambdify((x, y), c4.lhs)(_range, _range)),
)

# + Collapsed="false" persistent_id="ab2ff7fd-1f97-454b-99e5-5d060a76bab5" last_executed_text="test_prob.intersection_points()" execution_event_id="9524f42f-b881-4d19-b19f-4141590034b4"
test_prob.intersection_points()

# + Collapsed="false" persistent_id="7c42e469-6394-4f02-9473-298836b2cf62"

