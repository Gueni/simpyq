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
