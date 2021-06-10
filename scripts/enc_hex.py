import binascii
import main
import os
import platform
import sys

inputsec: str = 'None'

def encodehex():
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

    result = binascii.hexlify(inputsec.encode('ascii'))
    print('Convert result: '
          + result.decode('ascii'))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter text: ')
    sys.stdout.write("\033[F")
    print('')
    print('Encode: '
          + inputsec)
    encodehex()


print('DevScripts enc_hex.py')
print('Hex Encoder')
createinput()