
with open('file5.txt', 'r') as my_f:
    for line in my_f:
        sum = 0
        x = line.split()
        for i in range(len(x)):
            try:
                if int(x[i]) > 0:
                    sum += int(x[i])
            except ValueError:
                continue
        print(f'Количество занятий по предмету {x[0]} - {sum}')