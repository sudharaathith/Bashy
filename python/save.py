import sys
import os
from pathlib import Path
s = False
for i in sys.argv:
    if s:        
        if i.endswith('.py'):
            if os.path.exists(i):
                fun = i[:-3]
                addr = os.getcwd()+'/'+i
                rc = Path.home().joinpath('.bashrc').open('r')
                st= fun+"="
                if st not in rc.read():
                    rc = Path.home().joinpath('.bashrc').open('a')
                    alias = """alias %s'python -u "%s"'"""%(st, addr)
                    rc.write(alias)
                    os.system("echo 'Save Sucessful: '{}' is added to bashrc! '".format(fun))
                    rc.close()

                else:
                    os.system("echo 'Save error: {} Already exist!'".format(fun))

            else:
                os.system("echo 'Save error: {} does not exist!'".format(i))
        else:
            os.system("echo 'Save error: {} is not a python command!'".format(i))
    else:
        s = True