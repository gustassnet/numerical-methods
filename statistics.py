import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def Newton_graph(f, df, points):
    x_vals = np.linspace(-10, 10, 400)
    y_vals = [f(x) for x in x_vals]

    # Function
    plt.plot(x_vals, y_vals, color='blue', linewidth=2, label="f(x)")

    for i in range(len(points) - 1):
        x0 = points[i]
        x1 = points[i + 1]

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


def Newton_table(iterations):
    df_table = pd.DataFrame(
        iterations,
        columns=["Iteracija", "x_n", "f(x_n)", "Paklaida"]
    )
    print(df_table)