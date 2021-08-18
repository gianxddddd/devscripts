import main
import os
import platform

from pathlib import Path
from displayer import console

inputsec: str = 'None'

def check_os():
    if platform.system() == "Windows":
        print('---------------------------------------')
        print(console.err('ERROR: Windows system unsupported.'))
        print('Press any key to exit.')
        input()
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return

def create_alias():
    if len(inputsec) == 0:
        print(console.err('ERROR: Cannot have empty alias name.'))
        createinput()
        return
    if inputsec == 'exit':
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return

    print('---------------------------------------')
    print('Enter alias command: ')
    commandsec = input()
    console.rmline_by_count(2)
    print('Alias command: '
          + commandsec)
    print('---------------------------------------')
    if len(commandsec) == 0:
        print(console.err('ERROR: Cannot have empty alias command.'))
        createinput()
        return
    if commandsec == 'exit':
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return

    f = open(str(Path.home()) + '/.bashrc', 'r')

    if not "alias " + inputsec + "='" + commandsec + "'\n" in f.read():
        print('Command: Create alias')
        try:
            f2 = open(str(Path.home()) + '/.bashrc', 'a')
            f2.write("alias " + inputsec + "='" + commandsec + "'\n")
            print(console.success('SUCCESS: Alias created successfully!'))
            f2.close()
        except:
            print(console.err('ERROR: Failed to create alias.'))
    else:
        print(console.err('ERROR: Alias already exists.'))

    f.close()
    createinput()

def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter alias name: ')
    inputsec = input()
    console.rmline_by_count(2)
    print('Alias name: '
          + inputsec)
    create_alias()

check_os()
print(console.head('DevScripts alias_creator.py'))
print('Alias Creator')
createinput()