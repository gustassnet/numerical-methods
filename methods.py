import matplotlib.pyplot as plt
import numpy as np

def Newton_method(f, df, x0, eps):
    # 1. Find where tangent line to a function crosses x-axis
    # Formula: f`(x0) * (x - x0) + f(x0) = 0
    iterations = []
    x = x0 - f(x0) / df(x0)

    # x will be closer to the root that x0, so we will repeat the process
    while abs(x - x0) >= eps:
        x0 = x
        error = abs(x - x0)
        iterations.append([x0, f(x0), error])
        x = x0 - f(x0) / df(x0)
    return x, iterations


def iteration_method(g, x0, q, eps):
    x = g(x0)
    iterations = []

    while abs(x - x0) >= (1 - q) / q * eps:
        x0 = x
        x = g(x0)
        error = abs(x - x0)
        iterations.append([x0, g(x0), error])
    return x, iterations