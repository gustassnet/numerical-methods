from scipy.optimize import fsolve, root, newton_krylov, least_squares
import methods as m
import time
import matplotlib.pyplot as plt
import numpy as np


def G(X, A):
    return A @ X - m.F(X)


def generate_scipy_graph():
    N_values = list(range(10, 401, 10))

    times_fsolve = []
    times_root = []
    times_krylov = []
    times_ls = []

    for N in N_values:
        A = m.generate_matrixA(N)
        X0 = np.zeros(N)

        # fsolve
        start = time.time()
        fsolve(lambda x: G(x, A), X0)
        times_fsolve.append(time.time() - start)

        # root
        start = time.time()
        root(lambda x: G(x, A), X0, method='hybr')
        times_root.append(time.time() - start)

        # newton_krylov
        start = time.time()
        newton_krylov(lambda x: G(x, A), X0)
        times_krylov.append(time.time() - start)

        # least_squares
        start = time.time()
        least_squares(lambda x: G(x, A), X0)
        times_ls.append(time.time() - start)

    plt.figure()

    plt.plot(N_values, times_fsolve, label="fsolve")
    plt.plot(N_values, times_root, label="root")
    plt.plot(N_values, times_krylov, label="newton_krylov")
    plt.plot(N_values, times_ls, label="least_squares")

    plt.xlabel("N")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.grid()

    plt.show()