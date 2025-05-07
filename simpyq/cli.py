import argparse
import datetime
from pyfiglet import Figlet
from config import VERSION, AUTHOR
from core import run_query

def show_banner():
    f = Figlet(font='slant')
    print(f.renderText('simpyq'))
    print(f"Author: {AUTHOR}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Version: {VERSION}\n")

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
    show_banner()

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
