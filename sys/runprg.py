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
    except Exception as err:
        print(tn["prog404"] % (progname, str(err)))
        return
    try:
        prog.nlosrun()
        sys.path.remove(dir)
        del prog
    except AttributeError:
        print(tn["prognot"] % progname)
    except BaseException as err:
        print(tn["progerr"] % (progname, str(err.__class__)))