import main
import os
import platform

inputsec: str = 'None'

def binconv():
    if len(inputsec) == 0:
        print('---------------------------------------')
        print('ERROR: Cannot convert an empty text.')
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

    result = ' '.join(format(ord(x), 'b') for x in inputsec)
    '1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100'
    print('---------------------------------------')
    print('Convert: '
          + inputsec)
    print('Result: '
          + result)
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter text: ')
    inputsec = input()
    binconv()


print('DevScripts binary_conv.py')
print('Binary Converter')
createinput()