import json
import random
import os


DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "data",
    "compliments.json"
)


def get_compliment():
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        quotes = json.load(file)

    return random.choice(quotes)
