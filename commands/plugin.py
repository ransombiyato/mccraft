NAME = "plugin"
DESCRIPTION = "Manage MCCRAFT plugins."
USAGE = """mccraft plugin list
mccraft plugin search <name>
mccraft plugin install <file.py|name>
mccraft plugin info <plugin>
mccraft plugin remove <plugin>"""

import os
import shutil
import json
import importlib.util

PLUGINS_DIR = os.path.expanduser("~/mccraft/plugins")
REGISTRY_FILE = os.path.expanduser("~/mccraft/plugin_registry.json")


def load_plugin(path):

    spec = importlib.util.spec_from_file_location(
        os.path.basename(path)[:-3],
        path
    )

    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    return mod


def run(args=None):

    if not args:
        print(USAGE)
        return

    command = args[0]

    os.makedirs(PLUGINS_DIR, exist_ok=True)


    if command == "list":

        plugins = [
            file for file in os.listdir(PLUGINS_DIR)
            if file.endswith(".py") and file != "__init__.py"
        ]

        if not plugins:
            print("No plugins installed.")
            return

        print("Installed plugins:\n")

        for file in sorted(plugins):

            mod = load_plugin(
                os.path.join(PLUGINS_DIR, file)
            )

            print("⛏", getattr(mod, "NAME", file[:-3]))
            print("  ", getattr(mod, "DESCRIPTION", "No description."))
            print("   Usage:",
                  getattr(mod, "USAGE", "No usage info."))
            print()

        return


    if command == "search":

        if len(args) < 2:
            print("Usage: mccraft plugin search <name>")
            return

        if not os.path.exists(REGISTRY_FILE):
            print("Plugin registry not found.")
            return

        query = args[1].lower()

        with open(REGISTRY_FILE) as f:
            registry = json.load(f)

        found = False

        print("Plugin search results:\n")

        for name, data in registry.items():

            if query in name.lower():

                print("⛏", name)
                print("  ", data.get(
                    "description",
                    "No description."
                ))

                print()
                found = True

        if not found:
            print("No plugins found.")

        return


    if command == "install":

        if len(args) < 2:
            print("Usage: mccraft plugin install <file.py|name>")
            return

        target = args[1]

        file = target


        # Install from registry
        if not os.path.exists(file):

            if not os.path.exists(REGISTRY_FILE):
                print("Plugin registry not found.")
                return

            with open(REGISTRY_FILE) as f:
                registry = json.load(f)

            if target not in registry:
                print("Plugin not found in registry.")
                return

            file = registry[target].get("file")


        if not file or not os.path.exists(file):
            print("Plugin file not found.")
            return


        destination = os.path.join(
            PLUGINS_DIR,
            os.path.basename(file)
        )


        if os.path.abspath(file) == os.path.abspath(destination):
            print("Plugin already installed.")
            return


        shutil.copy(file, destination)

        print(
            "⛏ Installed plugin:",
            os.path.basename(file)
        )

        return


    if command == "info":

        if len(args) < 2:
            print("Usage: mccraft plugin info <plugin>")
            return

        plugin = args[1]

        if not plugin.endswith(".py"):
            plugin += ".py"


        path = os.path.join(
            PLUGINS_DIR,
            plugin
        )


        if not os.path.exists(path):
            print("Plugin not found.")
            return


        mod = load_plugin(path)

        print(
            "⛏ Plugin:",
            getattr(mod, "NAME", plugin[:-3])
        )

        print()
        print("Description:")
        print(
            " ",
            getattr(mod, "DESCRIPTION", "No description.")
        )

        print()
        print("Usage:")
        print(
            " ",
            getattr(mod, "USAGE", "No usage info.")
        )

        return


    if command == "remove":

        if len(args) < 2:
            print("Usage: mccraft plugin remove <plugin>")
            return


        plugin = args[1]

        if not plugin.endswith(".py"):
            plugin += ".py"


        path = os.path.join(
            PLUGINS_DIR,
            plugin
        )


        if not os.path.exists(path):
            print("Plugin not found.")
            return


        os.remove(path)

        print(
            "⛏ Removed plugin:",
            plugin[:-3]
        )

        return


    print("Unknown plugin command.")
