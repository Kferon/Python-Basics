from sys import argv

try:
    name, hours, earnings, prize = argv
    print(f' Заработная плата сотрудника: {(int(hours) * int(earnings) + int(prize))}')
except ValueError:
    print('Введено не число')
