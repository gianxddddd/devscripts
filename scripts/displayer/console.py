def rmline_by_count(count: int):
    for _ in range(count):
        print('\033[A                \033[A')

## used for printing with colors

def err(message):
    return '\033[91m' + message + '\033[0m'


def head(message):
    return '\033[95m' + message + '\033[0m'

def success(message):
    return '\033[92m' + message + '\033[0m'