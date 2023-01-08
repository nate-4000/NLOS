"""
NLOS file system handler.
"""
import os

def up():
    os.chdir("..")

rdir = "/"
trdir = os.getcwd().replace('\\',"/")

cwd = rdir

def flop(fn):
    file = open(trdir + fn)
    return file

def cd(path):
    global cwd
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
