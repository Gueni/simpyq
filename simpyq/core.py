import re
import numpy as np
import matplotlib.pyplot as plt
import datetime
import os
from constants import PLOT_DIR
from utils import log_result

def derive(x):
    return np.gradient(x)

def integr(x, dx):
    return np.trapz(x, dx=dx)

def mod(x):
    return x % 1

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
