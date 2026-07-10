import difflib
import sys
import importlib
import pkgutil
from pathlib import Path

COMMANDS = {}

# Directory where main.py is located
BASE_DIR = Path(__file__).resolve().parent


def load_commands():
    for folder in ["commands", "plugins"]:
        folder_path = BASE_DIR / folder

        if not folder_path.exists():
            continue

        for module in pkgutil.iter_modules([str(folder_path)]):
            mod = importlib.import_module(f"{folder}.{module.name}")

            func = getattr(mod, "run", None)

            if func:
                command_name = getattr(mod, "NAME", module.name)
                COMMANDS[command_name] = func


def suggest_command(command):
    matches = difflib.get_close_matches(command, COMMANDS.keys(), n=1)

    if matches:
        print(f"💡 Did you mean: {matches[0]}?")
    else:
        print("Run 'mccraft help' to see all available commands.")


def main():
    load_commands()

    if len(sys.argv) < 2:
        if "help" in COMMANDS:
            COMMANDS["help"]([])
        else:
            print("No help command found.")
        return

    command = sys.argv[1]

    if command in COMMANDS:
        COMMANDS[command](sys.argv[2:])
    else:
        print(f"Unknown command: {command}")
        suggest_command(command)


if __name__ == "__main__":
    main()
