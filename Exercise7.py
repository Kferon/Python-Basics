from math import factorial


def fact(n):
    for n in range(1, n+1):
        yield factorial(n)

x = 0

for el in fact(int(input('Введите число: '))):
    if x < 15:
        print(el)
        x += 1