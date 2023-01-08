"""
NLOS main kernel, running this will open the system
"""
print("initialising system")

import os

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

import login
import shell

welcometext = """
Welcome to NLOS, a fast(ish) operating system written in Python 3.
Type "help" for a list of commands supported.
All files and operations are sandboxed. (but not guaranteed)
"""

def run():
    user = login.login()
    cls()
    print(welcometext)
    shell.open(user)

run()