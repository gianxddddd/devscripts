import main
import os
import platform

inputsec: str = 'None'

def ext():
    if len(inputsec) == 0:
        print('ERROR: Cannot locate the specified path.')
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
    if not os.path.exists(inputsec):
        print('ERROR: Path does not exists or is a directory.')
        createinput()
        return
    if not os.path.exists('jadx/decompiled/'):
        os.makedirs('jadx/decompiled/')
        return

    os.system('sudo ' + main.defLocation
              + 'libs/jadx-1.2.0/bin/jadx'
              + ' -d '
              + 'jadx/decompiled/'
              + os.path.basename(inputsec).rsplit('.', 1)[0]
              + ' '
              + inputsec)
    print('---------------------------------------')
    print('Decompile successful!'
          + ' Decompiled files are located'
          + ' inside "jadx/decompiled/".')
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter DEX/APK path: ')
    print('\033[A                             \033[A')
    print('Decompile: ' + os.path.basename(inputsec))
    ext()


print('DevScripts jadx.py')
print('jadx - version 1.2.0')
createinput()