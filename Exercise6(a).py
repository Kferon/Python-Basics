from itertools import count
number = 0
check = True
n = int(input('Введите количество целых чисел, которое хотите сгенерировать: '))
for i in count(int(input('Введите число, с которого начать генерировать целые числа: '))):
        if number < n:
            print(i)
            number += 1
