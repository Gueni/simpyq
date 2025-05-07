## core.py
from model import interpret_query
from processor import execute_operation
from utils import load_csv, log_result, extract_signals
from plotter import handle_plot


def run_query(csv_file, save=False, log=False):
    df = load_csv(csv_file)

    while True:
        query = input("Enter your query (or 'exit'): ").strip()
        if query.lower() == 'exit':
            break

        try:
            intent = interpret_query(query, df.columns)
            result = execute_operation(df, intent)

            if intent['operation'] == 'plot':
                handle_plot(df, intent, save)
            else:
                print("Result:", result)

            if log:
                log_result(query, result)

        except Exception as e:
            print("Error:", str(e))
            if log:
                log_result(query, f"Error: {str(e)}")