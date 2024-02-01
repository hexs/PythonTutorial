import time
with open('1.Tutorial/3.ex.py') as f:
    srting = f.read()
print('\n'.join(f'{i:2}|  {sr}'for i,sr in enumerate(srting.split('\n'),start=1)))
try:
    exec(srting)
except Exception as e:
    print(e.args)
    for i in (e.args):
        if type(i) is tuple:
            for j in i:
                print('\t',j)
        else:
            print(i)