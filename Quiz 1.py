import random

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
wrong = []

with open('Quiz 1.txt') as f:
    string = f.read()
    qs = []

for i in string.split('\n--\n'):
    q_text = i.split('\n')[0]
    c_text = i.split('\n')[1:]
    c = []
    q = q_text
    a = ''
    for v in c_text:
        if v[-2:] == '<>':
            v = v[0:-2]
            a = v
        c.append(f'{v}')
    qs.append([q, c, a])

for q, c, a in qs:
    print(BLUE, BOLD, q, ENDC, sep='')
    random.shuffle(c)
    for i, v in enumerate(c):
        print('\t', YELLOW, chr(ord("a") + i), '.  ', v, ENDC, sep='')
    # print(a)
    while True:
        try:
            ip = input('(a, b, c or d) >')
            if ip in ['a', 'b', 'c', 'd']:
                x = ord(ip) - ord('a')
                if a == c[x]:
                    # cor
                    print(f'{GREEN}correct{ENDC}')
                else:
                    print(f'{RED}wrong{ENDC},  The correct answer is {GREEN}{a}{ENDC}')
                    wrong.append(q)
                break
        except:
            pass
    print()
