NAME = "package"
DESCRIPTION = "Create, build and install MCCRAFT packages."
USAGE = "mccraft package <create/build/install/search/repo>"

import json
import shutil
import zipfile
from pathlib import Path
from urllib.request import urlopen
from . import package_repo, package_search

BASE = Path(__file__).resolve().parent.parent

def create_package(name):
    package_dir = BASE / "packages" / name
    if package_dir.exists():
        print("❌ Package already exists.")
        return
    (package_dir / "plugins").mkdir(parents=True)
    (package_dir / "configs").mkdir(parents=True)
    with open(package_dir / "package.json","w") as f:
        json.dump({"name":name,"version":"1.0","description":"MCCRAFT package"},f,indent=4)
    print("✅ Created package:", name)

def install_folder(folder):
    for folder_name in ["plugins","configs"]:
        source = folder / folder_name
        if not source.exists():
            continue
        target = BASE / folder_name
        target.mkdir(exist_ok=True)
        for file in source.iterdir():
            dst = target / file.name
            if dst.exists():
                print("⚠️ Skipped duplicate:", file.name)
                continue
            shutil.copy(file,dst)
            print("Installed:", file.name)

def install_file_package(filename):
    package_file = Path(filename)
    if not package_file.exists():
        print("❌ Package file not found.")
        return
    temp = BASE / "temp_package"
    if temp.exists():
        shutil.rmtree(temp)
    temp.mkdir()
    with zipfile.ZipFile(package_file,"r") as z:
        z.extractall(temp)
    install_folder(temp)
    shutil.rmtree(temp)
    print("✅ Package installed.")

def install_from_repo(name):
    repo_file = BASE / "package_repos.json"
    if not repo_file.exists():
        return False
    with open(repo_file) as f:
        repos = json.load(f)
    for repo in repos.get("repos",[]):
        try:
            if repo.startswith("http"):
                with urlopen(repo) as r:
                    data=json.loads(r.read().decode())
            else:
                with open(repo) as f:
                    data=json.load(f)
        except Exception:
            continue
        for package in data.get("packages",[]):
            if package.get("name")==name:
                file = package.get("url") or package.get("file")
                if not file:
                    print("❌ Package URL missing.")
                    return True
                if repo.startswith("http") and not file.startswith("http"):
                    url = repo.rsplit("/",1)[0]+"/"+file
                    out = BASE / Path(file).name
                    with urlopen(url) as r:
                        out.write_bytes(r.read())
                    install_file_package(out)
                else:
                    install_file_package(file)
                return True
    return False

def install_package(name):
    package = BASE/"packages"/name
    if not package.exists():
        print("❌ Package not found locally.")
        return
    install_folder(package)

def build_package(name):
    package = BASE/"packages"/name
    if not package.exists():
        print("❌ Package not found.")
        return
    out = BASE/(name+".mcpkg")
    with zipfile.ZipFile(out,"w") as z:
        for file in package.rglob("*"):
            if file.is_file():
                z.write(file,file.relative_to(package))
    print("✅ Built:", out.name)

def run(args=None):
    if not args:
        print("Usage:")
        print("  mccraft package create <name>")
        print("  mccraft package build <name>")
        print("  mccraft package install <name|file.mcpkg>")
        print("  mccraft package search <name>")
        print("  mccraft package repo <add|list|remove> ...")
        return
    action=args[0]
    if action=="search":
        package_search.run(args[1:]); return
    if action=="repo":
        package_repo.run(args[1:]); return
    if len(args)<2:
        print("Missing package name."); return
    name=args[1]
    if action=="create":
        create_package(name)
    elif action=="build":
        build_package(name)
    elif action=="install":
        if name.endswith(".mcpkg"):
            install_file_package(name)
        elif not install_from_repo(name):
            install_package(name)
    else:
        print("Unknown package action.")

