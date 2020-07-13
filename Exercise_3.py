with open('file2.txt', 'r') as my_f:
    sum = 0
    money = []
    my_list = []
    for i in my_f:
        i = i.split()
        print(i)
        if int(i[1]) < 20000:
            my_list.append(i[0])
        money.append(int(i[1]))
    for x in range(len(money)):
        sum += money[x]
    print(f'Список людей с зарплатой ниже 20000: {my_list}. Средняя величина дохода сотрудников: {(sum/len(money))}')