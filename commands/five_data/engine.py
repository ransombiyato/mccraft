import random
import os
import sys

sys.path.append(os.path.dirname(__file__))

from commands.five_data.insult import get_insult
from commands.five_data.hopeful import get_hope
from commands.five_data.compliment import get_compliment

def run(args=None):
    if args is None:
        args = []

    categories = {
        "insult": get_insult,
        "insults": get_insult,

        "hopeful": get_hope,
        "hope": get_hope,
        "hopes": get_hope,

        "compliment": get_compliment,
        "compliments": get_compliment
    }

    print("⛏ MCCRAFT FIVE\n")

    # mccraft five
    # Default: 1 compliment
    if len(args) == 0:
        print("💚 " + get_compliment())
        return

    # mccraft five 3
    # Random mix
    if args[0].isdigit():
        amount = int(args[0])

        choices = [
            get_insult,
            get_hope,
            get_compliment
        ]

        for _ in range(amount):
            print("⛏ " + random.choice(choices)())
            print()

        return

    # mccraft five insult 5
    # mccraft five hopeful 10
    # mccraft five compliment 2
    category = args[0].lower()

    if category in categories:
        amount = 1

        if len(args) > 1 and args[1].isdigit():
            amount = int(args[1])

        for _ in range(amount):
            print("⛏ " + categories[category]())
            print()

        return

    print("❌ Unknown five option.")
    print("Usage:")
    print("  mccraft five")
    print("  mccraft five <number>")
    print("  mccraft five <compliment|insult|hopeful> <number>")


if __name__ == "__main__":
    run(sys.argv[1:])
