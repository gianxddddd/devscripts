import base64
import binascii
import main
import os
import platform

inputsec: str = 'None'

def decodebase32():
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
        result = base64.b32decode(inputsec.encode('ascii'))
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
    print('\033[A                             \033[A')
    print('Decode: '
          + inputsec)
    decodebase32()


print('DevScripts dec_base32.py')
print('Base32 Decoder')
createinput()