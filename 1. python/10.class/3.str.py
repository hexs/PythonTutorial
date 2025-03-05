from hexss.constants.terminal_color import *


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{BLUE}{self.name}{END}'


p1 = Person('John', 22)
print(p1)
print('name ', p1.name)
print('age  ', p1.age)

print()

p2 = Person('Jame', 25)
print(p2)
print('name ', p2.name)
print('age  ', p2.age)

