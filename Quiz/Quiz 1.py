import random
from hexss.constants.terminal_color import *

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
    print(BLUE, BOLD, q, END, sep='')
    random.shuffle(c)
    for i, v in enumerate(c):
        print('\t', YELLOW, chr(ord("a") + i), '.  ', v, END, sep='')
    # print(a)
    while True:
        try:
            ip = input('(a, b, c or d) >')
            if ip in ['a', 'b', 'c', 'd']:
                x = ord(ip) - ord('a')
                if a == c[x]:
                    # cor
                    print(f'{GREEN}correct{END}')
                else:
                    print(f'{RED}wrong{END},  The correct answer is {GREEN}{a}{END}')
                    wrong.append(q)
                break
        except:
            pass
    print()
