NAME = "restore"
DESCRIPTION = "Restore MCCRAFT backups"
USAGE = "mccraft restore"

import os
import shutil

HOME = os.path.expanduser("~")

BACKUP_DIR = os.path.join(HOME, ".mccraft", "backup")
TERMUX_DIR = os.path.join(HOME, ".termux")


def run(args=None):

    if not os.path.exists(BACKUP_DIR):
        print("No backup found.")
        return

    shutil.copytree(
        BACKUP_DIR,
        TERMUX_DIR,
        dirs_exist_ok=True
    )

    os.system("termux-reload-settings")

    print("⛏ MCCRAFT settings restored!")
