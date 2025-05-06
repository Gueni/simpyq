import pandas as pd
import matplotlib.pyplot as plt
import re
from utils import compute_rms, compute_avg, suggest_signal, log_result, save_plot
from mappings import action_synonyms, metric_synonyms ,HEADERS

def load_data(csv_file):
    from add_headers import add_headers_to_csv
    # Check if the CSV file already has headers
    with open(csv_file, 'r') as f:
            first_line = f.readline().strip()
            if not re.match(r'^[\w\s,]+$', first_line):
                print("Headers are missing. Adding headers...")
                add_headers_to_csv(csv_file)
            else:
                print("Headers already present. No changes made.")

    df = pd.read_csv(csv_file,header=None,names=HEADERS)
    df.columns = [col.strip().lower() for col in df.columns]
    return df

# utils.py (updated parse_query with fuzzy + synonym support)
import re
from difflib import get_close_matches
from mappings import action_synonyms, metric_synonyms, HEADERS

def normalize_action(query):
    for key in action_synonyms:
        if key in query:
            return action_synonyms[key]
    if "plot" in query:
        return "plot"
    elif "rms" in query:
        return "calculate", "rms"
    elif "average" in query or "mean" in query:
        return "calculate", "average"
    return None

def normalize_metric(query):
    for key in metric_synonyms:
        if key in query:
            return metric_synonyms[key]
    return None

def find_best_signal_match(query):
    lowered_query = query.lower()
    for col in HEADERS:
        if col.lower() in lowered_query:
            return col
    matches = get_close_matches(lowered_query, [col.lower() for col in HEADERS], n=1, cutoff=0.6)
    if matches:
        index = [col.lower() for col in HEADERS].index(matches[0])
        return HEADERS[index]
    return None

def parse_query(query):
    query = query.lower()
    parsed = {"action": None, "metric": None, "target": None}

    action_result = normalize_action(query)
    if isinstance(action_result, tuple):
        parsed["action"], parsed["metric"] = action_result
    else:
        parsed["action"] = action_result

    if not parsed["metric"]:
        parsed["metric"] = normalize_metric(query)

    parsed["target"] = find_best_signal_match(query)

    return parsed

def execute_query(query_dict, df, save=False, log=False):
    time = df.iloc[:, 0]
    signal_name = query_dict["target"]
    columns = df.columns

    if signal_name not in columns:
        suggestion = suggest_signal(signal_name, columns)
        print(f"Signal '{signal_name}' not found. Suggestion: {suggestion}")
        return

    signal = df[signal_name]
    result = None

    if query_dict["action"] == "plot":
        plt.plot(time, signal, label=signal_name)
        plt.xlabel("Time")
        plt.ylabel(signal_name)
        plt.title(f"{signal_name} vs Time")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        if save:
            save_plot(signal_name)
        else:
            plt.show()

    elif query_dict["action"] == "calculate":
        if query_dict["metric"] == "rms":
            result = compute_rms(signal)
            print(f"RMS of {signal_name}: {result:.3f}")
        elif query_dict["metric"] == "average":
            result = compute_avg(signal)
            print(f"Average of {signal_name}: {result:.3f}")

        if log and result is not None:
            log_result(signal_name, query_dict["metric"], result)

def interactive_mode(csv_file, save=False, log=False):
    df = load_data(csv_file)
    print("\nEnter a query or type 'exit' to quit.")
    while True:
        query = input("\nQuery: ")
        if query.lower() in ["exit", "quit"]:
            break
        query_dict = parse_query(query)
        if query_dict["action"] and query_dict["target"]:
            execute_query(query_dict, df, save, log)
        else:
            print("Unrecognized query format.")

def batch_mode(csv_file, query_file, save=False, log=False):
    df = load_data(csv_file)
    with open(query_file, "r") as f:
        queries = f.readlines()
    for q in queries:
        query_dict = parse_query(q.strip())
        if query_dict["action"] and query_dict["target"]:
            print(f"\nProcessing: {q.strip()}")
            execute_query(query_dict, df, save, log)
        else:
            print(f"Invalid query: {q.strip()}")
