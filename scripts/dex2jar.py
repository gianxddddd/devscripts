# Deprecated feature, use jadx instead.

import main
import os

inputsec: str = 'None'

def extdex():
    if len(inputsec) == 0:
        print('ERROR: Cannot locate the specified path.')
        createinput()
        return
    if inputsec == 'exit':
        print('---------------------------------------')
        print('Command: exit')
        print('Ending script process..')
        main.execscript(main.defLocation +
                        'scripts/main.py')
        return
    if not os.path.exists('dex2jar/decompiled/'):
        os.makedirs('dex2jar/decompiled/')

    print('---------------------------------------')
    print('Decompiling ' + os.path.basename(inputsec)
          + ' with Dex2Jar..')
    os.system('sudo sh ' + main.defLocation
              + 'libs/dex2jar-2.0/d2j-dex2jar.sh'
              + ' -f -o "'
              + 'dex2jar/decompiled/'
              + os.path.basename(inputsec).rsplit('.', 1)[0]
              + '.jar" '
              + inputsec)
    print('---------------------------------------')
    print('Decompile successful!'
          + ' Decompiled files are located'
          + ' inside "scripts/dex2jar/decompiled/".')
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter dex filepath: ')
    inputsec = input()
    extdex()


print("""NOTICE: This feature is deprecated"""
+ """ meaning the code won't be updated.""")
print('DevScripts dex2jar.py')
print('Dex2Jar Decompiler')
createinput()