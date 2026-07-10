#!/usr/bin/env python3

import os
import sys
import shutil

HOME = os.path.expanduser("~")
TERMUX_DIR = os.path.join(HOME, ".termux")
CONFIG_DIR = os.path.join(HOME, ".mccraft")
CONFIG_FILE = os.path.join(CONFIG_DIR, "current_font.txt")
FONTS_DIR = os.path.join(os.path.dirname(__file__), "fonts")


def help_menu():
    print("""
MCCRAFT v0.1

Usage:
  mccraft help
  mccraft version
  mccraft info

  mccraft font list
  mccraft font path
  mccraft font current
  mccraft font default
  mccraft font add <file.ttf>
  mccraft font <name>
""")


if len(sys.argv) < 2:
    help_menu()
    sys.exit()

command = sys.argv[1]


if command == "help":
    help_menu()

elif command == "version":
    print("MCCRAFT v0.1")

elif command == "info":

    print("MCCRAFT v0.1")

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            print("Current font:", f.read())
    else:
        print("Current font: default")

    count = 0

    if os.path.exists(FONTS_DIR):
        for file in os.listdir(FONTS_DIR):
            if file.endswith(".ttf"):
                count += 1

    print("Installed fonts:", count)

elif command == "font":

    if len(sys.argv) < 3:
        print("Usage: mccraft font <name|list|path|current|default|add>")
        sys.exit()

    subcommand = sys.argv[2]

    if subcommand == "list":

        os.makedirs(FONTS_DIR, exist_ok=True)

        print("Available fonts:\n")

        for file in os.listdir(FONTS_DIR):
            if file.endswith(".ttf"):
                print(" •", file[:-4])

    elif subcommand == "path":

        print(FONTS_DIR)

    elif subcommand == "add":

        if len(sys.argv) < 4:
            print("Usage: mccraft font add <file.ttf>")
            sys.exit()

        font_path = sys.argv[3]

        if not os.path.exists(font_path):
            print("Font file not found.")
            sys.exit()

        if not font_path.endswith(".ttf"):
            print("Only .ttf fonts are supported.")
            sys.exit()

        os.makedirs(FONTS_DIR, exist_ok=True)

        shutil.copy(
            font_path,
            os.path.join(FONTS_DIR, os.path.basename(font_path))
        )

        print("Added font:", os.path.basename(font_path)[:-4])

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

    else:

        font_file = os.path.join(FONTS_DIR, subcommand + ".ttf")

        if not os.path.exists(font_file):
            print(f"Font '{subcommand}' not found.")
            sys.exit()

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

else:
    print(f"Unknown command: {command}")