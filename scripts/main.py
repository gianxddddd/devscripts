import getpass
import help
import os
import platform
import sys

# If this raises error, change it to earlier versions of python interpreter.
# (Don't use Python 2 as the interpreter)
pythonExec = sys.executable

# If this raises FileNotFound, change the path.
defLocation = ' ' \
              + os.path.dirname(os.path.realpath(__file__))\
                  .strip('scripts')

inputsec: str = 'None'
printHistory = []


def printwsave(message):
    print(message)
    printHistory.append(message)


def execscript(path: str):
    printwsave('Executing python exec'
          ' with ' + inputsec + '..')

    if not os.path.exists('history'):
        os.mkdir('history')
        f = open('history/main.txt', 'w')
        f.write('\n'.join(printHistory))
        f.close()
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

    os.system(pythonExec + path)
    exit(0)


def promptscript():
    if len(inputsec) == 0:
        createinput()
        return
    if inputsec == 'help':
        help.help()
        createinput()
        return
    elif inputsec == 'exit':
        if platform.system() == 'Linux':
            os.system('clear')
        elif platform.system() == 'Windows':
            os.system('cls')

        exit(0)
    elif inputsec == 'enc_base64':
        execscript(' scripts/enc_base64.py')
    elif inputsec == 'dec_base64':
        execscript(' scripts/dec_base64.py')
    elif inputsec == 'enc_base32':
        execscript(' scripts/enc_base32.py')
    elif inputsec == 'dec_base32':
        execscript(' scripts/dec_base32.py')
    elif inputsec == 'enc_hex':
        execscript(' scripts/enc_hex.py')
    elif inputsec == 'dec_hex':
        execscript(' scripts/dec_hex.py')
    elif inputsec == 'art_ascii':
        execscript(' scripts/art_ascii.py')
    elif inputsec == 'jadx':
        execscript(' scripts/jadx.py')
    elif inputsec == 'youtube_dl':
        execscript(' scripts/yt_dl.py')
    elif inputsec == 'binary_conv':
        execscript(' scripts/binary_conv.py')
    else:
        printwsave("""ERROR: Cannot find the script you're looking for.""")
        createinput()


def createinput():
    global inputsec
    printwsave('---------------------------------------')
    try:
        inputsec = input().lower()
        sys.stdout.write("\033[F")
        print('Script: '
              + inputsec)
    except KeyboardInterrupt:
        # Added try catch method so
        # it won't raise KeyboardInterrupt.
        return
    promptscript()


def main():
    # If the main script is being re-set as the process again,
    # restore the previous session that the main script had.
    if os.path.exists('history'):
        f = open('history/main.txt', 'r')
        printwsave(f.read())
        f.close()
        os.remove('history/main.txt')
        os.rmdir('history')
        createinput()
        return
    if platform.system() == 'Linux':
        systemOS = 'GNU/Linux ' + platform.release()
    elif platform.system() == 'Windows':
        systemOS = 'Microsoft Windows ' + platform.version()

    printwsave('DevScripts main.py')
    printwsave('build 4403, 06-01-21 4:09:20')
    printwsave('Running on ' + systemOS)
    printwsave('Hello, ' + getpass.getuser()
          + '!')
    createinput()


if __name__ == '__main__':
    main()