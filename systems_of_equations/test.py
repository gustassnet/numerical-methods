import methods as m
import graph as g
import scipy_graph as s

# ------------------------------------------------------------------------------------------


N = 6
A = m.generate_matrixA(N)
epsilon = 1e-4

X = m.jacobi_method(A, epsilon)
print(X)




# ------------------------------------------------------------------------------------------