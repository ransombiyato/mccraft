import os
import sys

def doctor_command():
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

