# Numerical Methods in Python

## 1. Introduction

This project explores numerical methods for solving systems of nonlinear equations using Python.

It implements direct and iterative numerical methods, compares their performance with established methods available in the SciPy library, and analyzes execution times for systems of different sizes.

The project focuses on numerical algorithms, matrix operations, iterative convergence and computational performance.

## 2. Features

- Generation of structured coefficient matrices.
- Implementation of LU decomposition.
- Forward and backward substitution for solving linear systems.
- Implementation of the Jacobi iterative method.
- Nonlinear system solving using SciPy.
- Execution time measurement for different system sizes.
- Performance comparison between custom implementations and SciPy methods.
- Visualization of execution times using Matplotlib.

## 3. Implementation Details

### Matrix Generation

The `generate_matrixA()` function generates a structured square matrix of size N × N.

The matrix contains:
- `30` on the main diagonal.
- `-16` on the first diagonals above and below the main diagonal.
- `1` on the second diagonals above and below the main diagonal.

This matrix is used as the coefficient matrix in the numerical calculations.

### Nonlinear System

The `F()` function generates the right-hand side vector based on the current approximation of the solution.

The nonlinear system is expressed as:

\[
AX = F(X)
\]

where:
- `A` is the generated coefficient matrix.
- `X` is the unknown solution vector.
- `F(X)` is a nonlinear function of the current approximation.

### Direct Methods

The project implements LU decomposition to solve systems of equations.

The `LU_decomposition()` function decomposes the coefficient matrix into two matrices:

\[
A = LU
\]

where:
- `L` is a lower triangular matrix.
- `U` is an upper triangular matrix.

The resulting triangular systems are solved using:

- `reverse_from_top()` – forward substitution to solve \(LY = B\).
- `reverse_from_bottom()` – backward substitution to solve \(UX = Y\).

The `method()` function combines these operations in an iterative process, repeatedly updating the solution until the specified accuracy is reached.

### Iterative Methods

The project also implements the Jacobi iterative method.

The `jacobi_method()` function starts with an initial approximation and repeatedly calculates a new solution vector using the previous iteration.

The process continues until the maximum absolute difference between consecutive approximations is less than or equal to the specified tolerance.

### SciPy Methods

The project compares its implementations with numerical solvers available in `scipy.optimize`.

The following methods are evaluated:

- `fsolve()` – solves nonlinear equations using a root-finding algorithm.
- `root()` – provides different algorithms for finding roots of nonlinear systems.
- `newton_krylov()` – uses a Newton-Krylov method for solving nonlinear systems.
- `least_squares()` – solves nonlinear least-squares problems.

The nonlinear system is represented as:

\[
G(X) = AX - F(X) = 0
\]

Each SciPy method receives the same system and initial approximation for performance comparison.

## 4. Performance Analysis

The project measures the execution time of different numerical methods for systems of varying sizes.

### LU Decomposition and System Solving

The first performance experiment compares:

- LU decomposition.
- Forward and backward substitution.

The system size varies from 10 to 500.

Execution times are measured separately to distinguish the cost of matrix decomposition from the cost of solving the resulting triangular systems.

![LU Performance](My-time.png)

### SciPy Solver Comparison

The second experiment compares the execution times of:

- `fsolve()`
- `root()`
- `newton_krylov()`
- `least_squares()`

The system size varies from 10 to 400.

All methods are tested using the same generated matrices and initial solution vectors.

### Visualization

Matplotlib is used to visualize execution times.

The generated graphs allow comparison of computational performance as the system size increases.

## 5. Technologies Used

- **Python** – numerical algorithms and implementation.
- **NumPy** – matrix operations and numerical calculations.
- **SciPy** – reference numerical solvers.
- **Matplotlib** – execution time visualization.

## 6. Running

Run the main Python script:

```bash
python main.py
```

The program executes the selected numerical method and prints the calculated solution.

Performance comparison scripts can be executed separately to generate execution time graphs.