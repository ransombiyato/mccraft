NAME = "search"
DESCRIPTION = ""
USAGE = "mccraft search"

import os
import sys

FONTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "fonts"
)


def run(args=None):

    if len(sys.argv) < 3:
        print("Usage: mccraft search <text>")
        return

    query = sys.argv[2].lower()

    if not os.path.exists(FONTS_DIR):
        print("No fonts installed.")
        return

    matches = []

    for file in os.listdir(FONTS_DIR):
        if file.endswith(".ttf"):
            name = file[:-4]
            if query in name.lower():
                matches.append(name)

    if not matches:
        print("No matching fonts.")
        return

    print("Matching fonts:\n")

    for font in sorted(matches):
        print(" •", font)
