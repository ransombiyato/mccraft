NAME = "font"
DESCRIPTION = "Manage Termux fonts."

USAGE = """mccraft font list
mccraft font search <name>
mccraft font repo add <path/url>
mccraft font repo list
mccraft font repo remove <path/url>
mccraft font install <name|url>
mccraft font apply <font>
mccraft font current
mccraft font default
mccraft font add <file.ttf>"""

import os
import shutil
import json
from urllib.request import urlopen, urlretrieve


HOME = os.path.expanduser("~")

TERMUX_DIR = os.path.join(
    HOME,
    ".termux"
)

FONTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "fonts"
)

REPOS_FILE = os.path.expanduser(
    "~/mccraft/font_repos.json"
)


def get_repos():

    if not os.path.exists(REPOS_FILE):

        with open(REPOS_FILE, "w") as f:
            json.dump(
                {"repos": []},
                f,
                indent=4
            )

        return []

    with open(REPOS_FILE) as f:
        return json.load(f)["repos"]



def save_repos(repos):

    with open(REPOS_FILE, "w") as f:
        json.dump(
            {"repos": repos},
            f,
            indent=4
        )



def load_repo(repo):

    try:

        if repo.startswith("http"):

            with urlopen(repo) as r:
                return json.load(r)

        else:

            with open(repo) as f:
                return json.load(f)

    except Exception:

        return {}



def run(args=None):

    if not args:
        print(USAGE)
        return


    command = args[0]


    os.makedirs(
        FONTS_DIR,
        exist_ok=True
    )


    if command == "repo":

        if len(args) < 2:
            print(USAGE)
            return


        action = args[1]


        if action == "list":

            repos = get_repos()

            if not repos:
                print("No font repos added.")
                return

            print("Font repos:\n")

            for repo in repos:
                print(" •", repo)

            return



        if action == "add":

            repo = args[2]

            repos = get_repos()

            if repo not in repos:

                repos.append(repo)
                save_repos(repos)

                print("⛏ Added font repo:")
                print(repo)

            else:

                print("Repo already added.")

            return



        if action == "remove":

            repo = args[2]

            repos = get_repos()

            if repo in repos:

                repos.remove(repo)
                save_repos(repos)

                print("⛏ Removed font repo:")
                print(repo)

            else:

                print("Repo not found.")

            return



    if command == "search":

        query = args[1].lower()

        found = False

        print("⛏ Searching fonts...\n")


        for repo in get_repos():

            data = load_repo(repo)


            for name, info in data.items():

                if query in name.lower():

                    print("•", name)

                    print(
                        " ",
                        info.get(
                            "description",
                            "No description"
                        )
                    )

                    print()

                    found = True


        if not found:

            print("No fonts found.")

        return



    if command == "install":

        target = args[1]

        url = None
        filename = None


        if target.startswith("http"):

            url = target
            filename = target.split("/")[-1]


        else:

            for repo in get_repos():

                data = load_repo(repo)


                if target in data:

                    url = data[target]["url"]
                    filename = url.split("/")[-1]
                    break



        if not url:

            print("Font not found in repos.")
            return


        print("⛏ Downloading font...")


        urlretrieve(
            url,
            os.path.join(
                FONTS_DIR,
                filename
            )
        )


        print(
            "⛏ Installed:",
            filename
        )

        return



    if command == "apply":

        name = args[1]

        font_file = None


        for file in os.listdir(FONTS_DIR):

            if file.lower().replace(".ttf", "") == name.lower():

                font_file = os.path.join(
                    FONTS_DIR,
                    file
                )

                break



        if not font_file:

            print("Font not installed.")
            return



        os.makedirs(
            TERMUX_DIR,
            exist_ok=True
        )


        shutil.copy(
            font_file,
            os.path.join(
                TERMUX_DIR,
                "font.ttf"
            )
        )


        os.system(
            "termux-reload-settings"
        )


        print(
            "⛏ Applied font:",
            name
        )

        return



    if command == "list":

        fonts = [
            f.replace(".ttf", "")
            for f in os.listdir(FONTS_DIR)
            if f.endswith(".ttf")
        ]


        if not fonts:

            print("No fonts installed.")
            return


        print("Installed fonts:\n")

        for font in fonts:

            print(" •", font)

        return



    if command == "add":

        shutil.copy(
            args[1],
            FONTS_DIR
        )

        print("⛏ Font added.")
        return



    if command == "default":

        font = os.path.join(
            TERMUX_DIR,
            "font.ttf"
        )

        if os.path.exists(font):

            os.remove(font)


        os.system(
            "termux-reload-settings"
        )


        print("Default font restored.")

        return



    print("Font command not found.")
