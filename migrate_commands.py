import os
import re

COMMANDS_DIR = "commands"

for filename in os.listdir(COMMANDS_DIR):
    if not filename.endswith(".py"):
        continue
    if filename == "__init__.py":
        continue

    path = os.path.join(COMMANDS_DIR, filename)

    with open(path, "r") as f:
        content = f.read()

    command = filename[:-3]

    # Skip if already migrated
    if "def run(" in content:
        print(f"✓ {filename} already migrated")
        continue

    # Rename xxx_command -> run
    content = re.sub(
        rf"def\s+{command}_command\s*\(",
        "def run(",
        content
    )

    # Add metadata if missing
    if "NAME =" not in content:
        metadata = (
            f'NAME = "{command}"\n'
            f'DESCRIPTION = ""\n'
            f'USAGE = "mccraft {command}"\n\n'
        )
        content = metadata + content

    with open(path, "w") as f:
        f.write(content)

    print(f"✓ Migrated {filename}")

print("\nDone!")
