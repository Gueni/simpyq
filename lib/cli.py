#!/usr/bin/env python3
import argparse
from core import interactive_mode, batch_mode
from utils import ensure_output_folder

def main():
    parser = argparse.ArgumentParser(description="Natural Language Signal Query Tool")
    parser.add_argument("csv_file", help="Path to simulation CSV file")
    parser.add_argument("--save", action="store_true", help="Auto-save plots to output/")
    parser.add_argument("--log", action="store_true", help="Log results to output/log.txt")
    parser.add_argument("--batch", type=str, help="Path to query .txt file for batch mode")

    args = parser.parse_args()
    ensure_output_folder()

    if args.batch:
        batch_mode(args.csv_file, args.batch, save=args.save, log=args.log)
    else:
        interactive_mode(args.csv_file, save=args.save, log=args.log)

if __name__ == "__main__":
    main()
