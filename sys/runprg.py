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
        rc = prog.nlosrun()
        sys.path.remove(dir)
        del prog
        #if rc == None:
        #   print("warning: program %s did not return a response code")
    except AttributeError:
        print(tn["prognot"] % progname)
    except BaseException as err:
        print(tn["progerr"] % (progname, str(err.__class__)))
    except SystemExit:
        print(tn["progabr"] % progname)