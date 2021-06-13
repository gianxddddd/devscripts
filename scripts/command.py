## command.py is an Alias creator for Bash shell.
import main
import platform

from pathlib import Path

if platform.system() == 'Windows':
    main.execscript(' scripts/main.py')
    exit(0)

f = open(str(Path.home()) + '/.bashrc', 'r')

if "alias devscripts='sh " + main.defLocation + "devscript_linux.sh'" in f.read():
    pass
else:
    print('Create command')
    f2 = open(str(Path.home()) + '/.bashrc', 'a')
    f2.write("alias devscripts='sh " + main.defLocation + "devscript_linux.sh'")
    f2.close()

f.close()
main.execscript(' scripts/main.py')
exit(0)