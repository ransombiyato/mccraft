NAME = "package_search"
DESCRIPTION = "Search MCCRAFT packages."
USAGE = "mccraft package_search <name>"


import json
from pathlib import Path
from urllib.request import urlopen


BASE = Path(__file__).resolve().parent.parent

REPO_FILE = BASE / "package_repos.json"



def load_repo(repo):

    try:

        if repo.startswith("http"):

            with urlopen(repo) as response:

                return json.loads(
                    response.read().decode()
                )


        else:

            with open(repo) as f:

                return json.load(f)


    except Exception as e:

        print("⚠️ Failed loading repo:", repo)

        return None



def run(args=None):

    if not args:

        print("Usage:")
        print("  mccraft package_search <name>")
        return



    search = args[0].lower()



    if not REPO_FILE.exists():

        print("❌ No package repos.")
        return



    with open(REPO_FILE) as f:

        repos = json.load(f)



    found = False



    print("🔎 Searching packages...")



    for repo in repos.get("repos", []):


        data = load_repo(repo)


        if not data:

            continue



        for package in data.get("packages", []):


            name = package.get("name", "")



            if search in name.lower():


                found = True


                print("")
                print("📦", name)
                print("Description:", package.get("description", ""))
                print("Version:", package.get("version", ""))
                print("File:", package.get("file", ""))



    if not found:

        print("No packages found.")
