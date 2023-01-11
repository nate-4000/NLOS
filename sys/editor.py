"""
NLOS editor.
Attempts to be a mix of vi and ed.
"""

import gas
import filesys

tn = gas.get("sys/names.json")

def intput(text):
    ex = False
    while not ex:
        d = input(text)
        try:
            d = int(d)
            ex = True
        except:
            print("invalid input, must be integer")
    return d



def edit(filename):
    try:
        x = open(filename, "a")
    except:
        print(tn[404])
        return
    ex = False
    d = filesys.cat(filename).splitlines()
    i = 0
    for m in d:
        i+=1
        print(i, m)
    while not ex:
        stdin = input()
        if stdin == ":e":
            x.close()
            ex = True
        elif stdin == ":r":
            l = intput("line number: ") - 1
            t = input("text to replace: ")
            x.close()
            filesys.repline(filename, l, t)
            x = open(filename, "a")
        elif stdin == ":u":
            d = filesys.cat(filename).splitlines()
            i = 0
            for m in d:
                i+=1
                print(i, m)
        else:
            x.write(stdin + "\n")