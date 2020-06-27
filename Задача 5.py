revenue = int(input('Выручка компаниии: '))
costs = int(input('Издержки компании: '))
profit = revenue - costs
if profit > 0:
    print('Финансовый результат фирмы: прибыль')
    print('Рентабельность выручки(ROS): ', profit / revenue)
    workers = int(input('Введите численность сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника: ', profit / workers)
else:
    print('Финансовый результат фирмы: убыток')
