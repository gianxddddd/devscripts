import base64
import main
import os
import platform

inputsec: str = 'None'

def encodebase64():
    if len(inputsec) == 0:
        print('---------------------------------------')
        print('ERROR: Cannot encode an empty text.')
        createinput()
        return
    if inputsec == 'exit':
        print('---------------------------------------')
        print('Command: exit')
        print('Ending script process..')

        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        os.system(main.pythonExec + ' scripts/main.py')
        exit(0)
        return

    result = base64.b64encode(inputsec.encode('ascii'))
    print('---------------------------------------')
    print('Encode: '
          + inputsec)
    print('Convert result: '
          + result.decode('ascii'))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    inputsec = input('Enter text: ')
    encodebase64()


print('DevScripts enc_base64.py')
print('Base64 Encoder')
createinput()