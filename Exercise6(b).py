from itertools import cycle


my_list = [13, 'nemo', True, 104]
num = 0
again = int(input('Введите количество повторений списка: '))
for x in cycle(my_list):
    if num < again*len(my_list):
        print(x)
        num += 1