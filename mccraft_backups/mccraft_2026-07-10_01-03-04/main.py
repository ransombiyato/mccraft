import sys

from commands.setup import setup_command
from commands.remove import remove_command
from commands.search import search_command
from commands.stats import stats_command
from commands.doctor import doctor_command
from commands.help import help_command
from commands.version import version_command
from commands.info import info_command
from commands.font import font_command

import sys
import importlib
import pkgutil

COMMANDS = {}

for module in pkgutil.iter_modules(["commands"]):
    mod = importlib.import_module(f"commands.{module.name}")

    func = getattr(mod, f"{module.name}_command", None)

    if func:
        COMMANDS[module.name] = func

def main():
    if len(sys.argv) < 2:
        help_command()
        return

    command = sys.argv[1]

    if command in COMMANDS:
        COMMANDS[command]()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
