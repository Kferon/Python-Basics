season = [12, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11]
month = int(input('Введите номер месяца: '))
if month == season[0] or month == season[1] or month == season[2]:
    print('Зима')
elif month == season[3] or month == season[4] or month == season[5]:
    print('Весна')
elif month == season[6] or month == season[7] or month == season[8]:
    print('Лето')
elif month == season[9] or month == season[10] or month == season[11]:
    print('Осень')
else:
    print('Нет месяца с таким номером')
