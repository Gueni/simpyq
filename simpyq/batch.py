## batch.py
import os
from utils import load_csv
from model import interpret_query
from processor import execute_operation
from plotter import handle_plot
from utils import log_result


def run_batch(query_file, save=False, log=False):
    with open(query_file, 'r') as f:
        queries = [line.strip() for line in f if line.strip()]

    csv_files = [f for f in os.listdir(".") if f.endswith(".csv") and "utc" in f]
    for csv_file in csv_files:
        print(f"Processing: {csv_file}")
        df = load_csv(csv_file)
        for query in queries:
            try:
                intent = interpret_query(query, df.columns)
                result = execute_operation(df, intent)
                if intent['operation'] == 'plot':
                    handle_plot(df, intent, save)
                else:
                    print(f"{csv_file} | {query}: {result}")
                if log:
                    log_result(f"{csv_file} | {query}", result)
            except Exception as e:
                print(f"{csv_file} | {query} -> Error: {str(e)}")
                if log:
                    log_result(f"{csv_file} | {query}", f"Error: {str(e)}")