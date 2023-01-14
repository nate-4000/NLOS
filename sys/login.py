"""
NLOS login handler.
"""

import json
import hashlib
import filesys
import os
from gas import get, store

trdir = filesys.trdir

hashpwd = lambda a: int(hashlib.md5(a.encode("utf-8")).hexdigest(), 16)

tn = get("sys/names.json")


def tupdusrs():
    global usrs
    usrs = get("sys/shadow.json")


def updusrs():
    rdexec(tupdusrs)


def rdexec(func, args=[]):
    tempdir = os.getcwd()
    global usrs
    os.chdir(trdir)
    func(*args)
    os.chdir(tempdir)


# for x in usrs["users"]:
#    print(x["name"])


def login():
    while True:
        tusr = input(tn["uask"])
        tpass = input(tn["pask"])
        atlusr = chkusr(tusr, tpass)
        if atlusr is None:
            print(tn["wronglogin"])
        else:
            return atlusr


def chkusr(tusr, tpwd):
    updusrs()
    try:
        atlusr = next(obj for obj in usrs["users"] if obj["name"] == tusr)
    except:
        # print("not a valid user")
        return None
    if not str(atlusr["pwd"]) == str(hashpwd(tpwd)):
        return None
    else:
        return atlusr


def iaddusr():
    print(tn["usw"])
    taddusr = input(tn["uask"])
    taddpwd = input(tn["pask"])
    addusr(taddusr, hashpwd(taddpwd))


def addusr(usr, pwd):
    updusrs()
    usrs["users"].append({"name": usr, "pwd": pwd})
    rdexec(store, ["sys/shadow.json", usrs])
    updusrs()