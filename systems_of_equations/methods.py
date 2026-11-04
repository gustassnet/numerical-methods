import numpy as np


# ------------------------------------------------------------------------------------------
# DATA GENERATION

def generate_matrixA(N):
    matrixA = np.zeros((N, N), int)
    np.fill_diagonal(matrixA, 30)
    np.fill_diagonal(matrixA[1:], -16)
    np.fill_diagonal(matrixA[2:], 1)
    np.fill_diagonal(matrixA[:, 1:], -16)
    np.fill_diagonal(matrixA[:, 2:], 1)
    return matrixA


def F(X):
    N = len(X)
    B = np.zeros(N)
    c = 1 / (N + 1)**2                 # Constant that will be used for the function

    # First element
    B[0] = c + 2 * (X[1] - 0)**2

    # Middle elements
    for i in range(1, N - 1):
        B[i] = c + 2 * (X[i + 1] - X[i - 1])**2

    # Last element
    B[N - 1] = c + 2 * (0 - X[N - 2])**2
    return B


# ------------------------------------------------------------------------------------------
# EXACT METHODS
# For small systems n < 1000


def LU_decomposition(A):
    N = len(A)
    L = np.eye(N, dtype=float)
    U = np.copy(A).astype(float)

    for i in range(N):
        for j in range(i + 1, N):
            temp = U[j, i] / U[i, i]
            L[j, i] = temp
            U[j, i:] = U[j, i:] - temp * U[i, i:]
    return L, U


def reverse_from_top(L, B):
    N = len(L)
    Y = np.zeros(N, dtype=float)

    for i in range(N):
        sum = 0.0
        for j in range(i):
            sum += L[i, j] * Y[j]
        Y[i] = (B[i] - sum) / L[i, i]
    return Y


def reverse_from_bottom(U, Y):
    N = len(U)
    X = np.zeros(N, dtype=float)

    for i in range(N - 1, -1, -1):
        sum = 0.0
        for j in range(i + 1, N):
            sum += U[i, j] * X[j]
        X[i] = (Y[i] - sum) / U[i, i]
    return X


def method(A, epsilon):
    N = len(A)                         # Size of the matrix A
    X = np.zeros(N, dtype=float)       # Initial guess for the solution
    L, U = LU_decomposition(A)         # LU decomposition of matrix A

    while True:
        B = F(X)
        Y = reverse_from_top(L, B)
        X_new = reverse_from_bottom(U, Y)

        error = np.max(np.abs(X_new - X))
        X = X_new
        if error <= epsilon:
            break
    return X


# ------------------------------------------------------------------------------------------
# ITERATIVE METHODS
# For big systems n > 1000


def jacobi_method(A, epsilon):
    N = len(A)
    X = np.zeros(N, dtype=float)

    B = F(X)
    while True:
        X_new = np.zeros(N)

        for i in range(N):
            s = 0.0
            for j in range(N):
                if j != i:
                    s += A[i, j] * X[j]

            X_new[i] = (B[i] - s) / A[i, i]

        error = np.max(np.abs(X_new - X))
        X = X_new

        if error <= epsilon:
            break

    return X


# ------------------------------------------------------------------------------------------
