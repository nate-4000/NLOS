"""
NLOS program standard handler.
"""

import os
import gas
import sys



tn = gas.get("sys/names.json")


def run(progname, dir):
    # raise NotImplementedError
    sys.path.insert(0, dir)
    os.chdir(dir)
    try:
        prog = __import__(progname)
    except BaseException as err:
        print(tn["prog404"] % (progname, str(err)))
        return
    try:
        prog.nlosrun()
    except AttributeError:
        print(tn["prognot"] % progname)