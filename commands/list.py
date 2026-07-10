NAME = "list"
DESCRIPTION = ""
USAGE = "mccraft list"

import pkgutil

def run(args=None):
    print("MCCRAFT Commands:\n")

    for module in pkgutil.iter_modules(["commands"]):
        print(" - " + module.name)
