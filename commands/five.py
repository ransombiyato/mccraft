NAME = "five"
DESCRIPTION = "Get random compliments, insults, and hopeful messages"
USAGE = "mccraft five [amount] | mccraft five <compliment|insult|hopeful> <amount>"

from commands.five_data.engine import run as five_run

def run(args=None):
    if args is None:
        args = []

    five_run(args)
