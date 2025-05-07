import pandas as pd
from tabulate import tabulate

def load_csv(path):
    return pd.read_csv(path)

def print_table(df):
    headers = df.columns.tolist()
    total_cols = len(headers)
    col_width = max(max(len(str(h)) for h in headers), 10) + 4

    for block_start in range(0, total_cols, 4):
        block_end = min(block_start + 4, total_cols)
        block_headers = headers[block_start:block_end]
        block_indices = list(range(block_start, block_end))

        # Header
        print("+" + "+".join(["-" * col_width] * (len(block_headers) + 1)) + "+")
        print("|" + " signal ".center(col_width) + "|" + "|".join(h.center(col_width) for h in block_headers) + "|")
        print("|" + " index  ".center(col_width) + "|" + "|".join(str(i).center(col_width) for i in block_indices) + "|")
        print("+" + "+".join(["-" * col_width] * (len(block_headers) + 1)) + "+")
