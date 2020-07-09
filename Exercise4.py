my_list = list(map(int, input('Введите числа через пробел: ').split()))
print(f'Изначальный список без повторяющихся чисел: {[i for i in my_list if my_list.count(i) == 1]}')