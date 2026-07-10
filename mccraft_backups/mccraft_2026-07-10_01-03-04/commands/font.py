import os
import sys
import shutil

HOME = os.path.expanduser("~")
TERMUX_DIR = os.path.join(HOME, ".termux")
CONFIG_DIR = os.path.join(HOME, ".mccraft")
CONFIG_FILE = os.path.join(CONFIG_DIR, "current_font.txt")
FONTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fonts")


def font_command():

    if len(sys.argv) < 3:
        print("Usage: mccraft font <name|list|path|current|default|add>")
        return

    subcommand = sys.argv[2]

    os.makedirs(FONTS_DIR, exist_ok=True)

    if subcommand == "list":

        print("Available fonts:\n")

        for file in os.listdir(FONTS_DIR):
            if file.endswith(".ttf"):
                print(" •", file[:-4])

    elif subcommand == "path":

        print(FONTS_DIR)

    elif subcommand == "current":

        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as f:
                print("Current font:", f.read())
        else:
            print("Using default font")

    elif subcommand == "default":

        font = os.path.join(TERMUX_DIR, "font.ttf")

        if os.path.exists(font):
            os.remove(font)

        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)

        os.system("termux-reload-settings")

        print("Default font restored!")

    elif subcommand == "add":

        if len(sys.argv) < 4:
            print("Usage: mccraft font add <file.ttf>")
            return

        font_path = sys.argv[3]

        if not os.path.exists(font_path):
            print("Font not found.")
            return

        shutil.copy(
            font_path,
            os.path.join(FONTS_DIR, os.path.basename(font_path))
        )

        print("Added:", os.path.basename(font_path))

    else:

        font_file = os.path.join(FONTS_DIR, subcommand + ".ttf")

        if not os.path.exists(font_file):
            print(f"Font '{subcommand}' not found.")
            return

        os.makedirs(TERMUX_DIR, exist_ok=True)

        shutil.copy(
            font_file,
            os.path.join(TERMUX_DIR, "font.ttf")
        )

        os.makedirs(CONFIG_DIR, exist_ok=True)

        with open(CONFIG_FILE, "w") as f:
            f.write(subcommand)

        os.system("termux-reload-settings")

        print(f"⛏ Enabled font: {subcommand}")
