def mul_table(x: int):
    for i in range(1, 13):
        print(f'{x} x {i:2} = {i * x:2}')


def mul_table2(x: int):
    for i in range(1, 13):
        print(f'{x} x {i:2} = {i * x:{len(str(x * 12))}}')


mul_table(3)
print()
mul_table(11)
print()
mul_table2(159)
