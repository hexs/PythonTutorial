BLACK = '\033[90m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
PINK = '\033[95m'
CYAN = '\033[96m'
ENDC = '\033[0m'
BOLD = '\033[1m'
ITALICIZED = '\033[3m'
UNDERLINE = '\033[4m'

COLOR = {'BLACK': '\033[90m',
         'RED': '\033[91m',
         'GREEN': '\033[92m',
         'YELLOW': '\033[93m',
         'BLUE': '\033[94m',
         'PINK': '\033[95m',
         'CYAN': '\033[96m',

         'ENDC': '\033[0m',
         'BOLD': '\033[1m',
         'ITALICIZED': '\033[3m',
         'UNDERLINE': '\033[4m', }


def prunt(data, color=None):
    if color:
        print(COLOR[color.upper()], end='')
    print(data)
    print(COLOR['ENDC'], end='')


prunt(1+5, 'pink')
prunt(1+9)
# prunt(123).pink
