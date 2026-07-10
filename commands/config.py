NAME = "config"
DESCRIPTION = ""
USAGE = "mccraft config"

import os
import json

CONFIG = os.path.expanduser("~/mccraft/config.json")

def run(args=None):
    if not os.path.exists(CONFIG):
        with open(CONFIG, "w") as f:
            json.dump({"version": "0.1"}, f, indent=4)

    with open(CONFIG, "r") as f:
        data = json.load(f)

    print("MCCRAFT Config\n")

    for key, value in data.items():
        print(f"{key}: {value}")
