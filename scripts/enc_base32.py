import base64
import main
import os
import platform

from displayer import console

inputsec: str = 'None'

def encodebase32():
    if len(inputsec) == 0:
        print(console.err('ERROR: Cannot encode an empty text.'))
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

    result = base64.b32encode(inputsec.encode('ascii'))
    print(console.success('Convert result: '
          + result.decode('ascii')))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter text: ')
    inputsec = input()
    console.rmline_by_count(2)
    print('Encode: '
          + inputsec)
    encodebase32()


print(console.head('DevScripts enc_base32.py'))
print('Base32 Encoder')
createinput()