import matplotlib.pyplot as plt
import numpy as np

def Newton_graph(f, df, iterations):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [f(x) for x in x_vals]

    # Function
    plt.plot(x_vals, y_vals, color='blue', linewidth=2, label="f(x)")

    for i in range(len(iterations) - 1):
        x0 = iterations[i][0]
        x1 = iterations[i + 1][0]

        # Tangent line: f`(x0) * (x - x0) + f(x0)
        tangent = df(x0) * (x_vals - x0) + f(x0)
        plt.plot(x_vals, tangent, linestyle="--")

        # Intersection with Ox
        plt.scatter(x1, 0, color = 'red')

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    plt.title("Newton method")
    plt.grid(True, linestyle="--", linewidth = 0.5, color = 'green')
    plt.legend()
    plt.tight_layout()
    plt.show()


def Iteration_graph(g, iterations):
    x_vals = np.linspace(-2, 4, 400)
    y_vals = [g(x) for x in x_vals]

    # g(x)
    plt.plot(x_vals, y_vals, label="g(x)", color="blue")

    # y = x
    plt.plot(x_vals, x_vals, label="y = x", color="red")

    for i in range(len(iterations) - 1):
        x0 = iterations[i][0]
        x1 = iterations[i+1][0]

        plt.plot([x0, x0], [x0, x1], color="green")

        plt.plot([x0, x1], [x1, x1], color="green")

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    plt.title("Iteration method")
    plt.grid(True, linestyle="--", linewidth = 0.5, color = 'green')
    plt.legend()
    plt.show()


def System_graph():
    x = np.linspace(-6, 6, 400)
    y = np.linspace(-6, 6, 400)
    X, Y = np.meshgrid(x, y)

    # Functions
    F1 = X**2 + Y**2 - 25
    F2 = X**3 + Y**3 - 35

    plt.figure(figsize=(6,6))
    contour1 = plt.contour(X, Y, F1, levels=[0], colors='blue')
    contour2 = plt.contour(X, Y, F2, levels=[0], colors='red')

    plt.xlabel('x')
    plt.ylabel('y')

    plt.axhline(0, color='black')
    plt.axvline(0, color='black')

    plt.title('System of equations')
    plt.grid(True, linestyle="--", linewidth = 0.5, color = 'green')
    plt.show()