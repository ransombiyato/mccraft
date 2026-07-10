NAME = "backup"
DESCRIPTION = ""
USAGE = "mccraft backup"

import os
import shutil
from datetime import datetime

def run(args=None):
    home = os.path.expanduser("~")
    source = os.path.join(home, "mccraft")

    backup_dir = os.path.join(home, "mccraft_backups")
    os.makedirs(backup_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destination = os.path.join(backup_dir, f"mccraft_{timestamp}")

    shutil.copytree(source, destination)

    print("Backup created!")
    print(destination)

