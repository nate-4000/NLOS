import os
import login
import main

print("starting setup")
if not input("do you want to continue?").startswith("y"):
    exit()

print("setting up your user")
login.iaddusr()
print("your user has been added, login")
main.run()