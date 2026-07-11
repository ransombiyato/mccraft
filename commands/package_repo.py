NAME = "package_repo"
DESCRIPTION = "Manage MCCRAFT package repositories."
USAGE = "mccraft package_repo <add/list/remove> <url>"


import json
from pathlib import Path


BASE = Path(__file__).resolve().parent.parent

REPO_FILE = BASE / "package_repos.json"


def load_repos():

    if not REPO_FILE.exists():

        return {
            "repos": []
        }


    with open(REPO_FILE) as f:

        return json.load(f)



def save_repos(data):

    with open(REPO_FILE, "w") as f:

        json.dump(data, f, indent=4)



def add_repo(url):

    data = load_repos()


    if url in data["repos"]:

        print("⚠️ Repo already added.")
        return


    data["repos"].append(url)

    save_repos(data)

    print("✅ Package repo added.")



def list_repos():

    data = load_repos()


    if not data["repos"]:

        print("📦 No package repos.")

        return


    print("📦 Package Repositories:")


    for i, repo in enumerate(data["repos"], 1):

        print(f"{i}. {repo}")



def remove_repo(url):

    data = load_repos()


    if url not in data["repos"]:

        print("❌ Repo not found.")

        return


    data["repos"].remove(url)

    save_repos(data)

    print("🗑️ Package repo removed.")



def run(args=None):

    if not args:

        print("Usage:")
        print("  mccraft package_repo add <url>")
        print("  mccraft package_repo list")
        print("  mccraft package_repo remove <url>")
        return


    action = args[0]


    if action == "add":

        if len(args) < 2:

            print("Missing URL.")
            return

        add_repo(args[1])


    elif action == "list":

        list_repos()


    elif action == "remove":

        if len(args) < 2:

            print("Missing URL.")
            return

        remove_repo(args[1])


    else:

        print("Unknown action.")
