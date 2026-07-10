NAME = "get"
DESCRIPTION = ""
USAGE = "mccraft get"

import os
import json

CONFIG = os.path.expanduser("~/mccraft/config.json")

def run(args=None):
    if not args:
        print("Usage: mccraft get <key>")
        return

    key = args[0]

    if not os.path.exists(CONFIG):
        print("No config found")
        return

    with open(CONFIG, "r") as f:
        data = json.load(f)

    if key in data:
        print(data[key])
    else:
        print(f"{key} is not set")
