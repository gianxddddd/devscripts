import base64
import binascii
import main
import os
import platform

from displayer import console

inputsec: str = 'None'

def decodebase32():
    if len(inputsec) == 0:
        print(console.err('ERROR: Cannot decode an empty text.'))
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
        print(console.err('ERROR: Specified text is not encoded.'))
        createinput()
        return

    print(console.success('Convert result: '
          + result.decode('ascii')))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter base32 string: ')
    inputsec = input()
    console.rmline_by_count(2)
    print('Decode: '
          + inputsec)
    decodebase32()


print(console.head('DevScripts dec_base32.py'))
print('Base32 Decoder')
createinput()