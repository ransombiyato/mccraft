NAME = "info"
DESCRIPTION = ""
USAGE = "mccraft info"

import os

HOME = os.path.expanduser("~")
CONFIG_DIR = os.path.join(HOME, ".mccraft")
CONFIG_FILE = os.path.join(CONFIG_DIR, "current_font.txt")
FONTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fonts")


def run(args=None):
    print("MCCRAFT v0.1")

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            print("Current font:", f.read())
    else:
        print("Current font: default")

    os.makedirs(FONTS_DIR, exist_ok=True)

    count = len([f for f in os.listdir(FONTS_DIR) if f.endswith(".ttf")])

    print("Installed fonts:", count)
