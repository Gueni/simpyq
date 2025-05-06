import os
from difflib import get_close_matches
import matplotlib.pyplot as plt

def compute_rms(series):
    return (series**2).mean()**0.5

def compute_avg(series):
    return series.mean()

def suggest_signal(target, columns):
    matches = get_close_matches(target, columns, n=1, cutoff=0.6)
    return matches[0] if matches else None

def ensure_output_folder():
    os.makedirs("output", exist_ok=True)

def log_result(name, metric, value):
    with open("output/log.txt", "a") as f:
        f.write(f"{metric.upper()} of {name}: {value:.3f}\n")

def save_plot(signal_name):
    filename = f"output/{signal_name}_plot.png"
    plt.savefig(filename)
    print(f"Plot saved to {filename}")
    plt.close()
