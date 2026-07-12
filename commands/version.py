import os
import json

VERSION_FILE = os.path.expanduser("~/mccraft/version.json")

NAME = "version"
DESCRIPTION = "Show the current MCCRAFT version."
USAGE = "mccraft version"

def run(args=None):
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r") as f:
            data = json.load(f)

        print("MCCRAFT " + data["version"])
    else:
        print("Version unknown")
