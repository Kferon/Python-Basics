with open('file4.txt', 'w+') as my_f:
    string = input('Введите числа через пробел: ').split()
    print(sum(map(int, string)))