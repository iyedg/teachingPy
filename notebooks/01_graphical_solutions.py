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

# + Collapsed="false" persistent_id="7faa24a2-9c6b-4b9b-96b3-000fc621f83a" last_executed_text="%reload_ext autoreload\n%autoreload 2" execution_event_id="81807bc2-a916-453c-a8f9-ae36da77e339"
# %reload_ext autoreload
# %autoreload 2

# + Collapsed="false" execution_event_id="1d1b5d20-311c-40cf-a69e-af9834b453e3" last_executed_text="import matplotlib as mpl\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nimport numpy as np\nfrom sympy import Eq, lambdify, solve, sympify, symbols\n\nfrom palettable.tableau import BlueRed_12\nfrom teachingpy.operations_research.graphical import Constraint, GraphicalProblem\nfrom IPython.display import display\n\nmpl.rc(\"text\", usetex=True)\n# mpl.rcParams[\"axes.prop_cycle\"] = mpl.cycler(color=BlueRed_12.mpl_colors)" persistent_id="27d4caf3-2082-4138-8789-b13da81f93e5"
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
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

# + persistent_id="64fa0802-334d-4a5c-b9de-52ee218ca75f" last_executed_text="sns.set_style(\"whitegrid\")" execution_event_id="34b2b321-77fe-4294-8b69-9c145799ae34" Collapsed="false"
sns.set_style("whitegrid")

# + Collapsed="false" execution_event_id="6a9e04fc-4c40-4b1b-a3ff-ef27b859ff6d" last_executed_text="aspect_ratio = 16 / 9\nw = 12\nh = w / aspect_ratio\nfig, ax = plt.subplots(figsize=(w, h))\n\ntvs_radios_problem = GraphicalProblem()\n\nx_range = np.arange(0, 10)\n# c1 = Constraint(lhs=\"x - 2 * y\", rhs=\"2\", label=\"c1: $x - 2y \\geq 2$\", x_range=x_range)\nc1 = Constraint(\n    lhs=\"6 * x + 4 * y\", rhs=\"24\", label=\"c1: $x - 2y \\geq 2$\", x_range=x_range\n)\nc2 = Constraint(lhs=\"x + 2 * y\", rhs=\"6\", label=\"c2: $2 x + y \\leq 6$\", x_range=x_range)\nc3 = Constraint(lhs=\"y - x\", rhs=\"1\", label=\"c3: $3 x -y \\leq 4$\", x_range=x_range)\n# c4 = Constraint(lhs=\" 0 * x + y\", rhs=\"2\", label=\"c3: $3 x -y \\leq 4$\", x_range=x_range)\n\ntvs_radios_problem.add_constraints(c1, c2, c3)\ntvs_radios_problem.plot_constraints(lw=3)\n\n\nplt.xlim(0, 5)\nplt.ylim(0, 5)\nax.set_title(\"Three-constraint problem\")\nplt.grid(True)\nplt.tight_layout()" persistent_id="8d85ef9f-118e-4e6f-bc88-032f55fe1329"
# aspect_ratio = 16 / 9
aspect_ratio = 1
w = 8
h = w / aspect_ratio
fig, ax = plt.subplots(figsize=(w, h))

tvs_radios_problem = GraphicalProblem()

_range = np.arange(0, 10)

c1 = Constraint(lhs="6 * x + 4 * y", rhs="24", label="Labor constraint:\n$6x + 4y \leq 24$")
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

# + Collapsed="false" persistent_id="6166a0f7-fd35-415d-a004-da91a2b59491" last_executed_text="tvs_radios_problem.intersection_points()" execution_event_id="acc158ed-e8b2-445a-bb5c-10736a6c51c8"
tvs_radios_problem.intersection_points()

# + Collapsed="false" persistent_id="89d79e05-53e9-49d0-bdfc-308e821368f7" last_executed_text="import sympy" execution_event_id="d6a906a6-376a-448f-a9ed-bbcd264c9f9a"


# + persistent_id="ea846a02-e1c6-4fd8-b8a6-a68c68b1ce97" Collapsed="false"
k
