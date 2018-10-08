lst= []

def names():
    while True:
        name = input('Enter your name:')
        if name == '':
            break
        lst.append(name)
    return lst

names()
print(lst)

from collections import Counter

print(Counter(lst))


