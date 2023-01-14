"""
NLOS manual.
Made for dumb people.
"""

import gas

man = gas.get("sys/man.json")

tn = gas.get("sys/names.json")


def getpage(name):
    if name == "all":
        for key, value in man.items():
            print(" " * 4 + key)
            value  # value is put here so that my ide will stop yelling at me
        return
    try:
        print(tn["manintro"] % name)
        print(man[name])
    except KeyError:
        print(tn["man404"] % name)