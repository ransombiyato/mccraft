NAME = "help"
DESCRIPTION = "Show the help menu."
USAGE = "mccraft help"

import importlib
import pkgutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def run(args=None):
    if args:
        command = args[0]

        try:
            mod = importlib.import_module(f"commands.{command}")
        except ModuleNotFoundError:
            print(f"Unknown command: {command}")
            return

        print(f"Command: {getattr(mod, 'NAME', command)}")
        print()

        print("Description:")
        print(f"  {getattr(mod, 'DESCRIPTION', 'No description.')}")
        print()

        print("Usage:")
        print(f"  {getattr(mod, 'USAGE', f'mccraft {command}')}")
        print()

        help_text = getattr(mod, "HELP", None)
        if help_text:
            print(help_text.strip())

        return

    print("MCCRAFT v0.2\n")
    print("Available commands:\n")

    for module in sorted(
        pkgutil.iter_modules([str(BASE_DIR)]),
        key=lambda m: m.name
    ):
        mod = importlib.import_module(f"commands.{module.name}")

        name = getattr(mod, "NAME", module.name)
        desc = getattr(mod, "DESCRIPTION", "")

        print(f"  {name:<12} {desc}")
