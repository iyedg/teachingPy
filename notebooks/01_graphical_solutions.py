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

# + Collapsed="false" persistent_id="7faa24a2-9c6b-4b9b-96b3-000fc621f83a" last_executed_text="%reload_ext autoreload\n%autoreload 2" execution_event_id="961b88ed-4498-485f-9efc-dd00a83f632d"
# %reload_ext autoreload
# %autoreload 2

# + Collapsed="false" execution_event_id="1b955338-cc20-49e2-9be0-94dd553a447d" last_executed_text="import matplotlib as mpl\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport numpy as np\nfrom sympy import Eq, lambdify, solve, sympify, symbols\n\nfrom palettable.tableau import BlueRed_12\nfrom teachingpy.operations_research.graphical import Constraint, GraphicalProblem\n\nmpl.rc(\"text\", usetex=True)\nmpl.rcParams[\"axes.prop_cycle\"] = mpl.cycler(color=BlueRed_12.mpl_colors)" persistent_id="27d4caf3-2082-4138-8789-b13da81f93e5"
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sympy import Eq, lambdify, solve, sympify, symbols

from palettable.tableau import BlueRed_12
from teachingpy.operations_research.graphical import Constraint, GraphicalProblem

mpl.rc("text", usetex=True)
mpl.rcParams["axes.prop_cycle"] = mpl.cycler(color=BlueRed_12.mpl_colors)

# + [markdown] Collapsed="false" persistent_id="441b062d-a292-46d1-84f7-1dc3042b6279"
# $$y=mx+b$$
# $$y=m(x-x_0)+(b+y_0)$$

# + [markdown] Collapsed="false" persistent_id="0ae77ed8-2633-4fad-8123-eb24f756f365"
# http://www.geom.uiuc.edu/docs/reference/CRC-formulas/node9.html

# + persistent_id="64fa0802-334d-4a5c-b9de-52ee218ca75f" last_executed_text="plt.style.use(\"seaborn-talk\")" execution_event_id="0b1a0936-80c8-4fb5-a543-9cb29760c59d" Collapsed="false"
plt.style.use("seaborn-talk")

# + Collapsed="false" execution_event_id="6a9e04fc-4c40-4b1b-a3ff-ef27b859ff6d" last_executed_text="aspect_ratio = 16 / 9\nw = 12\nh = w / aspect_ratio\nfig, ax = plt.subplots(figsize=(w, h))\n\ntvs_radios_problem = GraphicalProblem()\n\nx_range = np.arange(0, 10)\n# c1 = Constraint(lhs=\"x - 2 * y\", rhs=\"2\", label=\"c1: $x - 2y \\geq 2$\", x_range=x_range)\nc1 = Constraint(\n    lhs=\"6 * x + 4 * y\", rhs=\"24\", label=\"c1: $x - 2y \\geq 2$\", x_range=x_range\n)\nc2 = Constraint(lhs=\"x + 2 * y\", rhs=\"6\", label=\"c2: $2 x + y \\leq 6$\", x_range=x_range)\nc3 = Constraint(lhs=\"y - x\", rhs=\"1\", label=\"c3: $3 x -y \\leq 4$\", x_range=x_range)\n# c4 = Constraint(lhs=\" 0 * x + y\", rhs=\"2\", label=\"c3: $3 x -y \\leq 4$\", x_range=x_range)\n\ntvs_radios_problem.add_constraints(c1, c2, c3)\ntvs_radios_problem.plot_constraints(lw=3)\n\n\nplt.xlim(0, 5)\nplt.ylim(0, 5)\nax.set_title(\"Three-constraint problem\")\nplt.grid(True)\nplt.tight_layout()" persistent_id="8d85ef9f-118e-4e6f-bc88-032f55fe1329"
aspect_ratio = 16 / 9
w = 12
h = w / aspect_ratio
fig, ax = plt.subplots(figsize=(w, h))

tvs_radios_problem = GraphicalProblem()

x_range = np.arange(0, 10)
# c1 = Constraint(lhs="x - 2 * y", rhs="2", label="c1: $x - 2y \geq 2$", x_range=x_range)
c1 = Constraint(
    lhs="6 * x + 4 * y", rhs="24", label="c1: $x - 2y \geq 2$", x_range=x_range
)
c2 = Constraint(lhs="x + 2 * y", rhs="6", label="c2: $2 x + y \leq 6$", x_range=x_range)
c3 = Constraint(lhs="y - x", rhs="1", label="c3: $3 x -y \leq 4$", x_range=x_range)
# c4 = Constraint(lhs=" 0 * x + y", rhs="2", label="c3: $3 x -y \leq 4$", x_range=x_range)

tvs_radios_problem.add_constraints(c1, c2, c3)
tvs_radios_problem.plot_constraints(lw=3)


plt.xlim(0, 5)
plt.ylim(0, 5)
ax.set_title("Three-constraint problem")
plt.grid(True)
plt.tight_layout()

# + Collapsed="false" persistent_id="e6bef59b-e681-4bbf-a673-31364f37d38d" last_executed_text="c4 = Constraint(lhs=\"x - 2\", rhs=\"0\", label=\"c3: $y = 2$\", x_range=x_range)" execution_event_id="473b5ff6-d4e0-498e-b1ec-bf77456ac1b0"
c4 = Constraint(lhs="x - 2", rhs="0", label="c3: $y = 2$", x_range=x_range)

# + Collapsed="false" persistent_id="ee46f6e5-4ba1-4473-b77f-f570bc85645a" last_executed_text="c4.evaluate()" execution_event_id="7c0f9b9e-e375-4b9c-bc57-893a88b0bdc6"
c4.evaluate()

# + Collapsed="false" persistent_id="4a054bd2-6a75-40be-924c-83176fbfa300" last_executed_text="x, y = symbols(\"x y\")" execution_event_id="2c779dea-5c41-48a1-aa4d-014b3bef2534"
x, y = symbols("x y")

# + Collapsed="false" persistent_id="ac6daf17-e274-4dd8-9070-0ee35e06ea7d" last_executed_text="lambdify(x, 2)(5)" execution_event_id="3e90e18f-451a-4acb-87c9-68967ddc0c35"
lambdify(x, 2)(5)

# + Collapsed="false" persistent_id="5730e12a-50b8-4c44-b417-10bdd15400ba" last_executed_text="solve(10 * x + x - 2)" execution_event_id="e6551909-9b77-4f41-9879-56751a37dd0f"
solve(10 * x + x - 2)

# + Collapsed="false" persistent_id="cc6e1c20-1f90-490c-b226-8c35bc2f3d50" last_executed_text="a, b = (sympify(\"x + y\")).free_symbols\n" execution_event_id="115471ed-5b0f-4580-bb3f-9a6795894ce2"
a, b = (sympify("x + y")).free_symbols


# + Collapsed="false" persistent_id="444003b2-1276-4576-bd32-576cbd44d414" last_executed_text="a == symbols(\"x\") or a == symbols(\"y\")" execution_event_id="0e637aeb-7fd7-43c6-8989-9c75ad375bac"
a == symbols("x") or a == symbols("y")

# + Collapsed="false" persistent_id="adc21573-f436-412a-a169-6023c62cfc71" last_executed_text="e = Eq(2 * x - 3 * y, 15)\nsolve(e, y)[0]" execution_event_id="8aaa66a0-316b-41d1-91db-7d9682cc2083"
e = Eq(2 * x - 3 * y, 15)
solve(e, y)[0]

# + Collapsed="false" persistent_id="0d6ed910-318f-4c61-b82f-03948c4df52c"

