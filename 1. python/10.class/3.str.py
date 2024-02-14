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


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return BLUE + self.name + ENDC


p1 = Person('John', 22)
print(p1)
print('name ', p1.name)
print('age  ', p1.age)

print()

p2 = Person('Jame', 25)
print(p2)
print('name ', p2.name)
print('age  ', p2.age)

