import pkgutil

def list_command():
    print("MCCRAFT Commands:\n")

    for module in pkgutil.iter_modules(["commands"]):
        print(" - " + module.name)
