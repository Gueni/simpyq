## utils.py
import os
import pandas as pd
import datetime


def load_csv(path):
    return pd.read_csv(path)


def log_result(query, result):
    os.makedirs("output/logs", exist_ok=True)
    with open("output/logs/log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Query: {query} | Result: {result}\n")


def extract_signals(df, signal_names):
    return [df[s] for s in signal_names if s in df.columns]