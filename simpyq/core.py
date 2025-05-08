<<<<<<< HEAD
import re
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
from constants import PLOT_DIR
from utils import log_result

def derive(x):
    return np.gradient(x)
=======
from interpreter import interpret_query
from utils import load_csv, log_result, extract_signals,handle_plot
import numpy as np

def execute_operation(df, intent):
    """Performs the intended operation on given signals in the DataFrame."""
    print("Available columns:", df.columns.tolist())

    signals = extract_signals(df, intent)
    op = intent["operation"]

    if op == "mean":
        return {sig: np.mean(df[sig]) for sig in signals}
    elif op == "rms":
        return {sig: np.sqrt(np.mean(df[sig] ** 2)) for sig in signals}
    elif op == "max":
        return {sig: np.max(df[sig]) for sig in signals}
    elif op == "min":
        return {sig: np.min(df[sig]) for sig in signals}
    elif op == "abs max":
        return {sig: np.max(np.abs(df[sig])) for sig in signals}
    elif op == "abs min":
        return {sig: np.min(np.abs(df[sig])) for sig in signals}
    elif op == "integr":
        return {sig: np.trapz(df[sig]) for sig in signals}
    elif op == "derive":
        return {sig: np.gradient(df[sig]).tolist() for sig in signals}
    elif op == "sqrt":
        return {sig: np.sqrt(df[sig]) for sig in signals}
    elif op == "sqr":
        return {sig: df[sig] ** 2 for sig in signals}
    elif op in ["+", "-", "*", "/", "div", "mod"]:
        if len(signals) != 2:
            raise ValueError(f"Binary operation '{op}' requires exactly two signals.")
        s1, s2 = df[signals[0]], df[signals[1]]

        if op == "+":
            return s1 + s2
        elif op == "-":
            return s1 - s2
        elif op == "*":
            return s1 * s2
        elif op == "/":
            return s1 / s2
        elif op == "div":
            return s1 // s2
        elif op == "mod":
            return s1 % s2
    else:
        raise ValueError(f"Unknown operation: {op}")
>>>>>>> 1253de11b126f9b1103a45177f5604a6a6c35ddf

def integr(x, dx):
    return np.trapz(x, dx=dx)

def mod(x):
    return x % 1

<<<<<<< HEAD
def div(x, y):
    return x // y

def parse_time_window(expr):
    match = re.search(r"\[(.*?)\]", expr)
    if not match:
        return None
    t_range = match.group(1).split(":")
    try:
        start = float(t_range[0]) if t_range[0] != '' else None
        end = float(t_range[1]) if len(t_range) > 1 and t_range[1] != '' else None
        return start, end
    except:
        return None

def evaluate_expression(expr, df):
    expr = expr.replace(' ', '')
    time_range = parse_time_window(expr)

    if time_range:
        t0, t1 = time_range
        time = df.iloc[:, 0].values
        mask = np.ones(len(df), dtype=bool)
        if t0 is not None:
            mask &= time >= t0
        if t1 is not None:
            mask &= time <= t1
        df = df[mask]
        expr = re.sub(r"\[.*?\]", "", expr)

    local_vars = {
        "mean": lambda x: np.mean(df.iloc[:, x].values),
        "rms": lambda x: np.sqrt(np.mean(df.iloc[:, x].values**2)),
        "max": lambda x: np.max(df.iloc[:, x].values),
        "min": lambda x: np.min(df.iloc[:, x].values),
        "absmax": lambda x: np.max(np.abs(df.iloc[:, x].values)),
        "absmin": lambda x: np.min(np.abs(df.iloc[:, x].values)),
        "sqr": lambda x: df.iloc[:, x].values ** 2,
        "sqrt": lambda x: np.sqrt(df.iloc[:, x].values),
        "derive": lambda x: derive(df.iloc[:, x].values),
        "integr": lambda x: integr(df.iloc[:, x].values, np.mean(np.diff(df.iloc[:, 0].values))),
        "mod": lambda x: mod(df.iloc[:, x].values),
        "div": lambda x, y: div(df.iloc[:, x].values, df.iloc[:, y].values)
    }

    if re.fullmatch(r"plot\(.*\)", expr):
        plot_expression(expr, df)
        return "Plotted."

    result = eval(expr, {**local_vars, "np": np})
    return result

def plot_expression(expr, df):
    time = df.iloc[:, 0].values
    content = expr[5:-1].strip()

    time_range = parse_time_window(content)
    if time_range:
        t0, t1 = time_range
        mask = np.ones(len(time), dtype=bool)
        if t0 is not None:
            mask &= time >= t0
        if t1 is not None:
            mask &= time <= t1
        df = df[mask]
        time = df.iloc[:, 0].values
        content = re.sub(r"\[.*?\]", "", content)

    indices = []
    if content == "all":
        indices = list(range(1, df.shape[1]))
    elif re.match(r"\[\d*:?\d*\]", content):
        rng = content.strip("[]").split(":")
        start = int(rng[0]) if rng[0] else 1
        end = int(rng[1]) if len(rng) > 1 and rng[1] else df.shape[1]
        indices = list(range(start, end))
    else:
        indices = [int(i) for i in content.split(',')]

    plt.figure(figsize=(50, 30))
    for i in indices:
        plt.plot(time, df.iloc[:, i].values, label=f"{df.columns[i]} (idx {i})")

    plt.title("Signals")
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True)

    plotname = f"plot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
    filepath = os.path.join(PLOT_DIR, plotname)
    plt.savefig(filepath)
    plt.close()
=======
        try:
            # Get the intent from the query
            intent = interpret_query(query, df.columns)
            print(f"Intent: {intent}")  # Debugging the intent structure

            # Ensure signals are valid
            signals = intent.get("signals", [])
            if not signals:
                raise ValueError("No valid signals extracted from the query.")

            # Execute the operation
            result = execute_operation(df, intent)

            # Plot if needed
            if intent["operation"] == "plot":
                handle_plot(df, intent, save)
            else:
                print("Result:", result)

            # Log the result if requested
            if log:
                log_result(query, result)

        except Exception as e:
            print("Error:", str(e))
            if log:
                log_result(query, f"Error: {str(e)}")
>>>>>>> 1253de11b126f9b1103a45177f5604a6a6c35ddf
