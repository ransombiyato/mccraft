import os
import shutil

HOME = os.path.expanduser("~")
TERMUX_DIR = os.path.join(HOME, ".termux")
CONFIG_DIR = os.path.join(HOME, ".mccraft")
FONTS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fonts")


def setup_command():
    print("⛏ Setting up MCCRAFT...\n")

    os.makedirs(TERMUX_DIR, exist_ok=True)
    os.makedirs(CONFIG_DIR, exist_ok=True)
    os.makedirs(FONTS_DIR, exist_ok=True)

    print("✅ .termux ready")
    print("✅ .mccraft ready")
    print("✅ fonts folder ready")

    if shutil.which("termux-reload-settings"):
        print("✅ termux-reload-settings found")
    else:
        print("❌ termux-reload-settings not found")

    print("\n🎉 MCCRAFT setup complete!")
