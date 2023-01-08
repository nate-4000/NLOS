"""
NLOS shell.
"""

import os
import filesys
import login

abouttext = """
NLOS is a operating system written in Python 3, and should be wrapped by the Linux kernel.
Commands are implemented weirdly, don't ask.
It will run if you run main.py... just try not to do any funny things.
todo: The system does run whatever executables it's wrapper can run... the wrapper can be found using the command "toplevel".
"""

comm = [
"help",
"toplevel",
"whoami",
"exit",
"cd",
"whereami",
"tlwai",
"ls",
"adduser",
"about",
"mkdir",
"eval",
"rm",
"rmdir"
]


def open(authuser):
    exit = False
    curusr = authuser
    curusrname = authuser["name"]
    while not exit:
        incomm = input(filesys.cwd + "> ")
        if incomm == "help":
            print("supported commands: ")
            for x in sorted(comm):
                print(" "*4+x)
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
                print("file not exist")
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
                print("operation not allowed")
            else:
                try:
                    os.remove(args)
                except:
                    print("file not exist")
        elif incomm.startswith("rmdir "):
            args = incomm.removeprefix("rmdir ")
            try:
                os.rmdir(args)
            except:
                print("file not exist")
        else:
            print("unknown command")
