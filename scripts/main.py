import getpass
import help
import os
import platform
import shutil
import sys

from displayer import console
from displayer import clock
from pathlib import Path

# If this raises error, change it to earlier versions of python interpreter.
# (Don't use Python 2 as the interpreter)
pythonExec = sys.executable

# If this raises FileNotFound, change the path.
defLocation = os.path.dirname(os.path.realpath(__file__))\
                  .strip('scripts')

inputsec: str = 'None'
printHistory = []


def printwsave(message):
    print(message)
    printHistory.append(message)


def execscript(path: str):
    printwsave('Script: ' + inputsec)
    printwsave(console.success('Launch: start script'))

    if not os.path.exists('history'):
        os.mkdir('history')
        f = open('history/main.txt', 'w')
        f.write('\n'.join(printHistory))
        f.close()
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

    os.system(pythonExec + path)
    exit(0)


def promptscript():
    if len(inputsec) == 0:
        printwsave(console.err('ERROR: Cannot find the script or command'
                   """ you're looking for."""))
        createinput()
        return
    if inputsec == 'help':
        printwsave('Command: entering help command...')
        help.help()
        createinput()
        return
    elif inputsec == 'exit':
        printwsave('Command: Killing main script...')
        
        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        exit(0)
    elif inputsec == 'clean':
        printwsave('Command: clean')

        printwsave('CLEAN: scripts')
        if os.path.exists('scripts/__pycache__') or \
                os.path.exists('scripts/displayer/__pycache__') or \
                os.path.exists('scripts/codehelper/__pycache__'):
            shutil.rmtree('scripts/__pycache__')
            shutil.rmtree('scripts/displayer/__pycache__')
            shutil.rmtree('scripts/codehelper/__pycache__')
        else:
            printwsave(console.err('ERROR: Scripts already cleaned.'))

        printwsave(console.success('SUCCESS: Done cleaning up files'))
        createinput()
    elif inputsec.startswith('echo'):
        printwsave('Command: echo')

        if inputsec != 'echo':
            printwsave(inputsec[4:])
        elif inputsec == 'echo':
            printwsave(console.err('ERROR: No arguments were given.'))

        createinput()
    elif os.path.exists('scripts/' + inputsec + '.py'):
        execscript(' scripts/' + inputsec + '.py')
    else:
        printwsave('Command: ' + inputsec)
        printwsave(console.err("""ERROR: Cannot find the script or command you're looking for."""))
        createinput()


def createalias():
    if platform.system() == 'Windows':
        return

    f = open(str(Path.home()) + '/.bashrc', 'r')

    if not "alias devscripts='sh " + defLocation + "devscript_linux.sh'" in f.read():
        print('Thank you for using DevScripts! You can now execute "devscripts" in the console.')
        try:
            f2 = open(str(Path.home()) + '/.bashrc', 'a')
            f2.write("alias devscripts='sh " + defLocation + "devscript_linux.sh'")
            f2.close()
        except:
            print(console.err('ERROR: Thank you for using DevScripts!'))

    f.close()


def createinput():
    global inputsec
    printwsave('---------------------------------------')
    try:
        inputsec = input().lower()
        console.rmline_by_count(1)
    except KeyboardInterrupt:
        # Added try catch method so
        # it won't raise KeyboardInterrupt.
        return
    promptscript()


def main():
    global systemOS
    createalias()

    # If the main script is being re-set as the process again,
    # restore the previous session that the main script had.
    if os.path.exists('history'):
        f = open('history/main.txt', 'r')
        printwsave(f.read())
        f.close()
        os.remove('history/main.txt')
        os.rmdir('history')
        createinput()
        return
    if platform.system() == 'Linux':
        systemOS = 'GNU/Linux ' + platform.release()
    elif platform.system() == 'Windows':
        systemOS = 'Microsoft Windows ' + platform.version()

    printwsave(console.head('DevScripts main.py'))
    printwsave('build 4405, '
               + clock.getdate()[:8] + ' '
               + clock.get24clock())
    printwsave('Running on ' + systemOS)
    printwsave('Hello, ' + getpass.getuser()
          + '!')
    createinput()


if __name__ == '__main__':
    main()
