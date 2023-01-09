"""
NLOS file system handler.
"""
import os

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
        print("attempting cd tree " + str(lpath))
        for t in lpath:
            if t == '':
                continue
            try:
                cd(t)
            except:
                print("unable to open directory " + t)
    else:
        if os.path.exists(path):
            try:
                os.chdir(path)
                cwd = os.getcwd()
                cwd = cwd.replace('\\',"/")
                cwd = cwd.removeprefix(trdir)
            except: # you lied to me
                print("directory is file")
        else:
            print("directory not found")

def ls():
    return os.listdir()

def cat(fn):
    with open(fn) as f:
        return f.read()

def mkdir(dn):
    os.makedirs(dn)
