NAME = "remove"
DESCRIPTION = ""
USAGE = "mccraft remove"

import os
import sys

FONTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "fonts"
)


def run(args=None):

    if len(sys.argv) < 3:
        print("Usage: mccraft remove <font>")
        return

    name = sys.argv[2]
    font = os.path.join(FONTS_DIR, name + ".ttf")

    if not os.path.exists(font):
        print(f"Font '{name}' not found.")
        return

    os.remove(font)

    print(f"⛏ Removed font: {name}")
