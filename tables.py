import pandas as pd

def table(iterations):
    df_table = pd.DataFrame(
        iterations,
        columns=["x_n", "f(x_n)", "Paklaida"]
    )
    print(df_table)