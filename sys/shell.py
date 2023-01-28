"""
NLOS shell.
"""

import os
import filesys
import login
import gas
import man
import editor
import runprg

tn = gas.get("sys/names.json")


abouttext = """
NLOS is a operating system written in Python 3, and should be wrapped by the Linux kernel.
If you try to mess with the command system, you will go to if/else hell.
It will run if you run main.py... just try not to do any funny things.
NLOS has its own program standard: type "man programs" for info on how to use it.
"""

comm = [
    "help",
    "toplevel",
    "whoami",
    "exit",
    "cd :",
    "whereami",
    "tlwai",
    "ls",
    "adduser",
    "about",
    "mkdir :",
    "eval :",
    "rm :",
    "rmdir :",
    "cat :",
    "man :",
    "mkfile :",
    "edit :",
    "run :"
]

def runbat(inlist: list):
    for comm in inlist:
        match comm.strip().split(" "):
            case ['print', *out]:
                for t in out:
                    print(t, end=" ")
                print()
            case _:
                print("warning, unknown command \"%s\"" % comm)

def runscr(filename):
    raise NotImplementedError
    with open(filename, "r") as prg:
        lprg = prg.readlines()
    runbat(lprg)

def open(authuser):
    exit = False
    curusr = authuser
    curusrname = authuser["name"]
    while not exit:
        incomm = input(filesys.cwd + "> ")
        if incomm == "help":
            print("supported commands: ")
            for x in sorted(comm):
                print(" " * 4 + x)
        elif incomm == "toplevel":
            print(os.name)
        elif incomm == "whoami":
            print(curusrname)
        elif incomm == "exit":
            exit = True
        elif incomm == "about":
            print(abouttext)
        elif incomm.startswith("cd "):
            args = incomm.removeprefix("cd ")
            filesys.cd(args)
        elif incomm == "whereami":
            print(filesys.cwd)
        elif incomm == "tlwai":
            print(os.getcwd())
        elif incomm == "ls":
            print(filesys.ls())
        elif incomm == "adduser":
            login.iaddusr()
        elif incomm == "about":
            print(abouttext)
        elif incomm.startswith("cat "):
            args = incomm.removeprefix("cat ")
            try:
                print(filesys.cat(args))
            except:
                print(tn["404"])
        elif incomm.startswith("mkdir "):
            args = incomm.removeprefix("mkdir ")
            filesys.mkdir(args)
        elif incomm.startswith("eval "):
            args = incomm.removeprefix("eval ")
            try:
                print(eval(args))
            except BaseException as err:
                print(str(err))
        elif incomm.startswith("rm "):
            args = incomm.removeprefix("rm ")
            if filesys.cwd.endswith("sys/") or filesys.cwd.endswith("sys"):
                print(tn["no"])
            else:
                try:
                    os.remove(args)
                except:
                    print(tn["404"])
        elif incomm.startswith("rmdir "):
            args = incomm.removeprefix("rmdir ")
            try:
                os.rmdir(args)
            except:
                print(tn["404"])
        elif incomm.startswith("man "):
            args = incomm.removeprefix("man ")
            man.getpage(args)
        elif incomm.startswith("mkfile "):
            args = incomm.removeprefix("mkfile ")
            filesys.mkf(args)
        elif incomm.startswith("edit "):
            args = incomm.removeprefix("edit ")
            editor.edit(args)
        elif incomm.startswith("run "):
            args = incomm.removeprefix("run ")
            runprg.run(args, os.getcwd())
        else:
            print(tn["notcomm"])
