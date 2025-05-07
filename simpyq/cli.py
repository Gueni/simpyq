import argparse
from utils import show_banner, log_result
from _io_ import load_csv, print_table
from core import evaluate_expression

def run_cli():
    # parser = argparse.ArgumentParser(description="Simpyq CLI")
    # parser.add_argument("--csv", type=str, required=True, help="CSV file path")
    # parser.add_argument("--tab", action="store_true", help="Show signal table and exit")

    # args = parser.parse_args()
    show_banner()
    path = input("Enter path to CSV file: ").strip()
    df = load_csv(path)
    print("CSV loaded. Type 'tab' to list signals. Type 'exit' to quit.\n")

    while True:
        query = input(">>> ").strip()
        if query == "exit":
            break
        elif query == "tab":
            print_table(df)
            continue

        try:
            result = evaluate_expression(query, df)
            print("Result:", result)
            log_result(query, result)
        except Exception as e:
            print("Error:", str(e))
            log_result(query, f"Error: {str(e)}")
