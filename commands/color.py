import os
import shutil

BACKUP_COLORS = os.path.expanduser("~/.termux/colors.properties.bak")

NAME = "color"
DESCRIPTION = "Manage Termux color schemes."
USAGE = """mccraft color list
mccraft color restore
mccraft color <scheme>"""

COLORS_DIR = os.path.expanduser("~/mccraft/colors")
TERMUX_COLORS = os.path.expanduser("~/.termux/colors.properties")


def run(args=None):

    if not args:
        print(USAGE)
        return

    command = args[0]

    if command == "list":
        if not os.path.exists(COLORS_DIR):
            print("No color schemes installed.")
            return

        print("Available color schemes:\n")

        for file in sorted(os.listdir(COLORS_DIR)):
            if file.endswith(".properties"):
                print(" ", file[:-11])

        return

    if command == "restore":
        if not os.path.exists(BACKUP_COLORS):
            print("No backup found.")
            return

        shutil.copy(BACKUP_COLORS, TERMUX_COLORS)
        os.system("termux-reload-settings")

        print("✓ Restored previous color scheme.")
        return

    scheme = os.path.join(COLORS_DIR, f"{command}.properties")

    if not os.path.exists(scheme):
        print(f"Color scheme '{command}' not found.")
        print("Run 'mccraft color list' to see available color schemes.")
        return

    os.makedirs(os.path.dirname(TERMUX_COLORS), exist_ok=True)

    shutil.copy(scheme, TERMUX_COLORS)

    os.system("termux-reload-settings")

    print(f"✓ Applied color scheme: {command}")
