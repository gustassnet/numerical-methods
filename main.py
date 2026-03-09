import methods as mth
import tables as tbl
import graphs as gr
import math

# ------------------------------------------------------------------------------------------
# FUNCTIONS AND DERIVATIVES


# Original function was 3 * sin(x) = x - 1
# We will solve f(x) = 0, where f(x) = 3 * sin(x) - x + 1
# The derivative of f(x) is f`(x) = 3 * cos(x) - 1

f = lambda x: 3 * math.sin(x) - x + 1
df = lambda x: 3 * math.cos(x) - 1

g = lambda x: math.asin((x - 1) / 3)


# ------------------------------------------------------------------------------------------
# NEWTON METHOD


# Newton method test cases: x0 = {0, -2, 4}
x, iterations = mth.Newton_method(f, df, 4, 0.000001)

tbl.table(iterations)
gr.Newton_graph(f, df, iterations)


# ------------------------------------------------------------------------------------------
# ITERATION METHOD


# Second root
q = math.sqrt(5) / 5
x, iterations = mth.iteration_method(g, 2.5, q, 0.000001)

tbl.table(iterations)
gr.Iteration_graph(g, iterations)

# Second root
x, iterations = mth.iteration_method(g, 0, q, 0.000001)
tbl.table(iterations)
gr.Iteration_graph(g, iterations)


# ------------------------------------------------------------------------------------------