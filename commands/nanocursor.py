NAME = "nanocursor"
DESCRIPTION = "Manage Nano's vertical guide stripe."
USAGE = "mccraft nanocursor [columns|off|default|list|help|preview [column]|color <color|off|list>]"

import os
import shutil
from difflib import get_close_matches


NANORC = os.path.expanduser("~/.nanorc")
DEFAULT_COLUMN = 80


VALID_COLORS = {
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
    "brightblack",
    "brightred",
    "brightgreen",
    "brightyellow",
    "brightblue",
    "brightmagenta",
    "brightcyan",
    "brightwhite",
}


def success(msg):
    print(f"\033[92m✓\033[0m {msg}")


def error(msg):
    print(f"\033[91m✗\033[0m {msg}")


def info(msg):
    print(f"\033[96mℹ\033[0m {msg}")


def warning(msg):
    print(f"\033[93m⚠\033[0m {msg}")


def normalize(line):
    return " ".join(line.strip().split())


def load_lines():
    if os.path.exists(NANORC):
        with open(NANORC, "r") as f:
            return f.readlines()
    return []


def save_lines(lines):
    with open(NANORC, "w") as f:
        f.writelines(lines)


def remove_setting(lines, setting):
    return [
        line for line in lines
        if not normalize(line).startswith(setting)
    ]


def get_setting(lines, setting):
    for line in lines:
        stripped = normalize(line)

        if stripped.startswith(setting):
            parts = stripped.split(maxsplit=2)

            if len(parts) >= 3:
                return parts[2]

    return None


def show_status():
    lines = load_lines()

    stripe = get_setting(lines, "set guidestripe")
    color = get_setting(lines, "set stripecolor")

    print("Nano Cursor")
    print("-----------")

    if stripe:
        success(f"Guide stripe : column {stripe}")
    else:
        warning("Guide stripe : disabled")

    if color:
        success(f"Stripe color : {color}")
    else:
        warning("Stripe color : default")


def preview(column=None):
    if column is None:
        current = get_setting(load_lines(), "set guidestripe")

        if current:
            column = int(current)
        else:
            column = DEFAULT_COLUMN

    if column < 1 or column > 200:
        error("Preview column must be between 1 and 200.")
        return

    print("Nano Guide Preview")
    print("------------------")

    max_col = max(80, ((column // 10) + 1) * 10)

    tens = ""
    ones = ""

    for i in range(1, max_col + 1):
        tens += str((i // 10) % 10)
        ones += str(i % 10)

    print(tens)
    print(ones)
    print(" " * (column - 1) + "│")

    print()
    info(f"Guide stripe preview at column {column}")


def run(args=None):

    if shutil.which("nano") is None:
        error("Nano is not installed.")
        return


    if not args or args[0].lower() in ("list", "help"):
        show_status()
        return


    if args[0].lower() == "preview":

        if len(args) == 1:
            preview()
            return

        try:
            preview(int(args[1]))
        except ValueError:
            error("Preview column must be an integer.")

        return


    cmd = args[0].lower()
    lines = load_lines()


    if cmd == "color":

        if len(args) < 2:
            error("Usage: mccraft nanocursor color <color|off|list>")
            return


        value = args[1].lower()


        if value == "list":
            print("Available stripe colors:")
            print()

            for color in sorted(VALID_COLORS):
                print(f"  {color}")

            return


        lines = remove_setting(lines, "set stripecolor")


        if value == "off":
            save_lines(lines)
            success("Stripe color reset.")
            info("Close and reopen Nano.")
            return


        if value not in VALID_COLORS:
            error(f"Invalid color '{value}'.")
            info("Run 'mccraft nanocursor color list'.")
            return


        lines.append(f"set stripecolor {value}\n")

        save_lines(lines)

        success(f"Stripe color set to {value}.")
        info("Close and reopen Nano.")
        return


    if cmd == "off":

        lines = remove_setting(lines, "set guidestripe")
        save_lines(lines)

        success("Guide stripe disabled.")
        info("Close and reopen Nano.")
        return


    if cmd == "default":
        cmd = str(DEFAULT_COLUMN)


    if not cmd.isdigit():

        error(f"Unknown option '{cmd}'.")

        match = get_close_matches(
            cmd,
            ["color", "default", "off", "list", "help", "preview"],
            n=1,
        )

        if match:
            info(f"Did you mean '{match[0]}'?")

        return


    column = int(cmd)


    if not 1 <= column <= 500:
        error("Column must be between 1 and 500.")
        return


    lines = remove_setting(lines, "set guidestripe")
    lines.append(f"set guidestripe {column}\n")

    save_lines(lines)

    success(f"Guide stripe set to column {column}.")
    info("Close and reopen Nano.")
