import base64
import binascii
import main
import os
import platform
import sys

inputsec: str = 'None'

def decodebase64():
    if len(inputsec) == 0:
        print('ERROR: Cannot decode an empty text.')
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
    try:
        result = base64.b64decode(inputsec.encode('ascii'))
    except binascii.Error:
        print('ERROR: Specified text is not encoded.')
        createinput()
        return

    print('Convert result: '
          + result.decode('ascii'))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter text: ')
    sys.stdout.write("\033[F")
    print('')
    print('Decode: '
          + inputsec)
    decodebase64()


print('DevScripts dec_base64.py')
print('Base64 Decoder')
createinput()