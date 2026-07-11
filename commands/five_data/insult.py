import json
import random
import os


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "data",
    "insults.json"
)


def get_insult():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        insults = json.load(f)

    return random.choice(insults)
