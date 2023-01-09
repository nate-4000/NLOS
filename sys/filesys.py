"""
NLOS file system handler.
"""

import os
import gas

tn = gas.get("sys/names.json")

def up():
    os.chdir("..")

rdir = "/"
trdir = os.getcwd().replace('\\',"/")

cwd = rdir

def uflop(fn):
    f = open(trdir + fn)
    return f

def cd(path):
    global cwd
    if path.startswith("/"):
        # raise NotImplementedError
        os.chdir(trdir)
        cwd = "/"
        if path == "/":
            return
        lpath = path.split("/")
        # print("attempting cd tree " + str(lpath))
        for t in lpath:
            if t == '':
                continue
            try:
                cd(t)
            except:
                print(tn["cddir404"] % t)
    else:
        if os.path.exists(path):
            try:
                os.chdir(path)
                cwd = os.getcwd()
                cwd = cwd.replace('\\',"/")
                cwd = cwd.removeprefix(trdir)
            except: # you lied to me
                print(tn["dirisfile"])
        else:
            print(tn["dir404"])

def ls():
    return os.listdir()

def cat(fn):
    try:
        with open(fn) as f:
            return f.read()
    except FileNotFoundError:
        print(tn["404"])

def mkdir(dn):
    os.makedirs(dn)
