"""
NLOS program standard handler.
"""

import os
import gas
import sys



tn = gas.get("sys/names.json")
rtc = gas.get("sys/rct.json")

def run(progname, dir):
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
        if rc == None:
            print(tn["progabr"] % progname)
        elif str(rc) in rtc.keys():
            print(tn["progcde"] % (progname, rc, rtc[str(rc)]))
        elif type(rc) is int and rc < 256:
            print(tn["progcodeinvalid"] % (progname, rc))
        else:
            print(tn["pcdebad"] % progname)
    except AttributeError:
        print(tn["prognot"] % progname)
    except BaseException as err:
        print(tn["progerr"] % (progname, str(err.__class__)))