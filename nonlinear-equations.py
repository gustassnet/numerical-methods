import statistics as st
import math


def Newton_method(f, df, x0, eps):
    # 1. Find where tangent line to a function crosses x-axis
    # Formula: f`(x0) * (x - x0) + f(x0) = 0
    i = 0
    points = [x0]
    iterations = []
    x = x0 - f(x0) / df(x0)

    # x will be closer to the root that x0, so we will repeat the process
    while abs(x - x0) >= eps:
        x0 = x
        points.append(x0)
        error = abs(x - x0)
        iterations.append([i, x0, f(x0), error])
        x = x0 - f(x0) / df(x0)
        i += 1
    return x, points, iterations


# Original function was 3 * sin(x) = (x + 1)
# We will solve f(x) = 0, where f(x) = 3 * sin(x) - x - 1
# The derivative of f(x) is f`(x) = 3 * cos(x) - 1

f = lambda x: 3 * math.sin(x) - x - 1
df = lambda x: 3 * math.cos(x) - 1


# Newton method test cases: x0 = {0, -2, 4}
root, points, iterations = Newton_method(f, df, 4, 0.001)

st.Newton_table(iterations)
st.Newton_graph(f, df, points)
