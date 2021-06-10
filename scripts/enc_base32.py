import base64
import main
import os
import platform

inputsec: str = 'None'

def encodebase32():
    if len(inputsec) == 0:
        print('ERROR: Cannot encode an empty text.')
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
    print('Convert result: '
          + result.decode('ascii'))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter text: ')
    print("\x1B[F\x1B[2K", end='')
    print('Encode: '
          + inputsec)
    encodebase32()


print('DevScripts enc_base32.py')
print('Base32 Encoder')
createinput()