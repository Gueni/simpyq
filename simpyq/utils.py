<<<<<<< HEAD
from pyfiglet import Figlet
import datetime
import os
from constants import LOG_DIR, AUTHOR, VERSION

def show_banner():
    f = Figlet(font='slant')
    print(f.renderText('simpyq'))
    print(f"Author: {AUTHOR}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Version: {VERSION}\n")

def log_result(query, result):
    with open(os.path.join(LOG_DIR, "log.txt"), "a") as f:
        f.write(f"[{datetime.datetime.now()}] {query} => {result}\n")
=======
import os
import pandas as pd
import datetime
import matplotlib.pyplot as plt

def load_csv(path):
    return pd.read_csv(path)


def log_result(query, result):
    os.makedirs("output/logs", exist_ok=True)
    with open("output/logs/log.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Query: {query} | Result: {result}\n")


import difflib

def extract_signals(query, columns):
    # Ensure you're working with strings
    if not isinstance(query, str):
        raise ValueError("Query must be a string.")

    matches = []
    for word in query.lower().split():
        close = difflib.get_close_matches(word, [col.lower() for col in columns], n=1, cutoff=0.6)
        if close:
            match = next((col for col in columns if col.lower() == close[0]), None)
            if match and match not in matches:
                matches.append(match)
    return matches



def handle_plot(df, intent, save):
    signals = intent['signals']
    df[signals].plot(title=f"Plot of {', '.join(signals)}")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid(True)
    if save:
        os.makedirs("output/plots", exist_ok=True)
        filename = f"output/plots/plot_{'_'.join(signals)}.png"
        plt.savefig(filename)
        print(f"Plot saved to {filename}")
    else:
        plt.show()
>>>>>>> 1253de11b126f9b1103a45177f5604a6a6c35ddf
