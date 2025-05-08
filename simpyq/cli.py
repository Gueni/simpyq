import argparse
<<<<<<< HEAD
from utils import show_banner, log_result
from _io_ import load_csv, print_table
from core import evaluate_expression
=======
import datetime
from pyfiglet import Figlet
from config import VERSION, AUTHOR
from core import run_query
>>>>>>> 1253de11b126f9b1103a45177f5604a6a6c35ddf

def run_cli():
    # parser = argparse.ArgumentParser(description="Simpyq CLI")
    # parser.add_argument("--csv", type=str, required=True, help="CSV file path")
    # parser.add_argument("--tab", action="store_true", help="Show signal table and exit")

<<<<<<< HEAD
    # args = parser.parse_args()
=======
def parse_train_argument(train_arg):
    parts = train_arg.split(' --op ')
    if len(parts) != 2:
        print("❌ Error: '--train' format should be 'query --op operation --sig signal1,signal2,...'")
        return

    query = parts[0].strip()
    op_sig_parts = parts[1].split(' --sig ')
    if len(op_sig_parts) != 2:
        print("❌ Error: '--train' format should be 'query --op operation --sig signal1,signal2,...'")
        return

    op = op_sig_parts[0].strip()
    signals = [s.strip() for s in op_sig_parts[1].split(',')]
    
    
    print(f"✅ Training with new example:\n   ➤ Query: {query}\n   ➤ Operation: {op}\n   ➤ Signals: {signals}")

def main():
>>>>>>> 1253de11b126f9b1103a45177f5604a6a6c35ddf
    show_banner()
    path = input("Enter path to CSV file: ").strip()
    df = load_csv(path)
    print("CSV loaded. Type 'tab' to list signals. Type 'exit' to quit.\n")

<<<<<<< HEAD
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
=======
    parser = argparse.ArgumentParser(description="Natural Language Signal Query Tool")
    parser.add_argument("csv_file", nargs="?", help="Path to simulation CSV file")
    parser.add_argument("--save", action="store_true", help="Auto-save plots to output/plots/")
    parser.add_argument("--log", action="store_true", help="Log results to output/logs/log.txt")
    parser.add_argument("-help", type=str, help="Help for a specific command")
    parser.add_argument("--help_all", action="store_true", help="Help for all commands")
    parser.add_argument("--train", type=str, help="Train with a new query (format: 'query --op operation --sig signal')")

    args = parser.parse_args()

    if args.help_all:
        parser.print_help()
        return

    if args.train:
        parse_train_argument(args.train)
        return

    if args.csv_file:
        run_query(args.csv_file, args.save, args.log)
    else:
        print("⚠️  No input provided.\n")
        parser.print_help()

if __name__ == "__main__":
    main()
>>>>>>> 1253de11b126f9b1103a45177f5604a6a6c35ddf
