book = {
    'name': 'ภาษาพาที',
    'number': 100,
    'price': 99
}

for i in book:
    print(i)
print()

for i in book.values():
    print(i)
print()

for k, v in book.items():
    print(k, v)
print()

for k, v in book.items():
    print(f'value of {k:7}is {v}')
print()
