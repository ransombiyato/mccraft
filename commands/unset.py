NAME = "unset"
DESCRIPTION = ""
USAGE = "mccraft unset"

import os
import json

CONFIG = os.path.expanduser("~/mccraft/config.json")

def run(args=None):
    if not args:
        print("Usage: mccraft unset <key>")
        return

    key = args[0]

    if not os.path.exists(CONFIG):
        print("No config found")
        return

    with open(CONFIG, "r") as f:
        data = json.load(f)

    if key in data:
        del data[key]

        with open(CONFIG, "w") as f:
            json.dump(data, f, indent=4)

        print(f"Removed {key}")
    else:
        print(f"{key} is not set")
