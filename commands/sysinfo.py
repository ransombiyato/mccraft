NAME = "sysinfo"
DESCRIPTION = ""
USAGE = "mccraft sysinfo"

import os
import platform
import sys

def run(args=None):
    print("MCCRAFT System Info\n")

    print("OS:", platform.system())
    print("Machine:", platform.machine())
    print("Python:", sys.version.split()[0])
    print("Home:", os.path.expanduser("~"))

