import os

VERSION = "1.0"
AUTHOR = "Mohamed Gueni"

PLOT_DIR = "simpyq/output/plots"
LOG_DIR = "simpyq/output/logs"

os.makedirs(PLOT_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)
