from math import factorial

def fact():
    for el in {factorial(int(input('введите номер элемента')))}:
        yield el

f = fact()

print(f)
for el in f:
    print(el)