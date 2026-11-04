import time
import matplotlib.pyplot as plt
import methods as m
import numpy as np

def generate_time_graph():
    N_values = list(range(10, 501, 10))

    times_LU = []
    times_solve = []

    for N in N_values:
        A = m.generate_matrixA(N)

        # LU decomposition
        start = time.time()
        L, U = m.LU_decomposition(A)
        end = time.time()
        times_LU.append(end - start)

        #  Solve LY = B and UX = Y
        X = np.zeros(N)
        B = m.F(X)

        start = time.time()
        Y = m.reverse_from_top(L, B)
        X_new = m.reverse_from_bottom(U, Y)
        end = time.time()
        times_solve.append(end - start)

    plt.figure()

    plt.plot(N_values, times_LU, label='LU dekompozicija')
    plt.plot(N_values, times_solve, label='LY + UX sprendimas')

    plt.xlabel("N")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.grid()

    plt.show()