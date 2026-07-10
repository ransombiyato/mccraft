NAME = "status"
DESCRIPTION = ""
USAGE = "mccraft status"

import os
import pkgutil

def run(args=None):
    print("MCCRAFT Status\n")

    commands = []

    for module in pkgutil.iter_modules(["commands"]):
        commands.append(module.name)

    print("Version: 0.1")
    print("Commands loaded:", len(commands))

    if os.path.exists(os.path.expanduser("~/mccraft/config.json")):
        print("Config: Found")
    else:
        print("Config: Missing")

