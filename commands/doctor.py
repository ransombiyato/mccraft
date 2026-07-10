NAME = "doctor"
DESCRIPTION = ""
USAGE = "mccraft doctor"

import os
import sys

def run(args=None):
    print("MCCRAFT Doctor\n")

    print("✓ Python:", sys.version.split()[0])

    if os.path.exists(os.path.expanduser("~/mccraft")):
        print("✓ mccraft folder found")
    else:
        print("✗ mccraft folder missing")

    if os.path.exists(os.path.expanduser("~/mccraft/commands")):
        print("✓ commands folder found")
    else:
        print("✗ commands folder missing")

