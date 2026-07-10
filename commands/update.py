NAME = "update"
DESCRIPTION = "Check for MCCRAFT updates."
USAGE = "mccraft update"

import os
import json

VERSION_FILE = os.path.expanduser("~/mccraft/version.json")
UPDATE_FILE = os.path.expanduser("~/mccraft/update.json")


def run(args=None):

    print("⛏ MCCRAFT Update\n")

    current = "unknown"
    latest = "unknown"

    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE) as f:
            current = json.load(f).get("version", "unknown")

    if os.path.exists(UPDATE_FILE):
        with open(UPDATE_FILE) as f:
            latest = json.load(f).get("latest", "unknown")

    print("Current:", current)
    print("Latest: ", latest)

    if current == latest:
        print("\n✅ MCCRAFT is up to date!")
    else:
        print("\n⬆ Update available!")
        print("Run: mccraft update apply")
