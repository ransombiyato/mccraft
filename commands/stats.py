NAME = "stats"
DESCRIPTION = ""
USAGE = "mccraft stats"

import os

HOME = os.path.expanduser("~")
CONFIG_DIR = os.path.join(HOME, ".mccraft")
CONFIG_FILE = os.path.join(CONFIG_DIR, "current_font.txt")
FONTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fonts")


def run(args=None):
    print("⛏ MCCRAFT Stats\n")

    count = 0

    if os.path.exists(FONTS_DIR):
        for file in os.listdir(FONTS_DIR):
            if file.endswith(".ttf"):
                count += 1

    print("Installed fonts:", count)

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            print("Current font:", f.read())
    else:
        print("Current font: default")

    print("Version: 0.1")
