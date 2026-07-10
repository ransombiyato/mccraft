NAME = "set"
DESCRIPTION = ""
USAGE = "mccraft set"

import os
import json

CONFIG = os.path.expanduser("~/mccraft/config.json")

def run(args=None):
    if not args or len(args) < 2:
        print("Usage: mccraft set <key> <value>")
        return

    key = args[0]
    value = " ".join(args[1:])

    if os.path.exists(CONFIG):
        with open(CONFIG, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[key] = value

    with open(CONFIG, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Set {key} = {value}")
