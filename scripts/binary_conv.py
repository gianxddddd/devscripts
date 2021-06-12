import main
import os
import platform

from displayer import console

inputsec: str = 'None'

def binconv():
    if len(inputsec) == 0:
        print(console.err('ERROR: Cannot convert an empty text.'))
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

    result = ' '.join(format(ord(x), 'b') for x in inputsec)
    '1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100'
    print(console.success('Result: '
          + result))
    createinput()


def createinput():
    global inputsec
    print('---------------------------------------')
    print('Enter binary code: ')
    inputsec = input()
    console.rmline_by_count(2)
    print('Convert: '
          + inputsec)
    binconv()


print(console.head('DevScripts binary_conv.py'))
print('Binary Converter')
createinput()