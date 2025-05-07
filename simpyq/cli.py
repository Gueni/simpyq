import argparse
import datetime
from pyfiglet import Figlet
from config import VERSION, AUTHOR
from core import run_query
from batch import run_batch

def show_banner():
    f = Figlet(font='slant')
    print(f.renderText('simpyq'))
    print(f"Author: {AUTHOR}")
    print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Version: {VERSION}\n")

def main():
    show_banner()

    parser = argparse.ArgumentParser(description="Natural Language Signal Query Tool")
    parser.add_argument("csv_file", nargs="?", help="Path to simulation CSV file")
    parser.add_argument("--save", action="store_true", help="Auto-save plots to output/plots/")
    parser.add_argument("--log", action="store_true", help="Log results to output/logs/log.txt")
    parser.add_argument("--batch", type=str, help="Path to query .txt file for batch mode")
    parser.add_argument("-help", type=str, help="Help for a specific command")
    parser.add_argument("--help_all", action="store_true", help="Help for all commands")
    args = parser.parse_args()

    if args.help_all:
        parser.print_help()
        return

    if args.batch:
        run_batch(args.batch, args.save, args.log)
    elif args.csv_file:
        run_query(args.csv_file, args.save, args.log)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
