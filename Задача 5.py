my_rate = [7, 5, 3, 3, 2]
while True:
    try:
        number = int(input('Введите число: '))
    except ValueError:
        print('Введено не число')
    for i in range(len(my_rate)):
        if my_rate[i] == number:
            my_rate.insert(i+1, number)
            break
        elif number > my_rate[0]:
            my_rate.insert(0, number)
            break
        elif number < my_rate[-1]:
            my_rate.append(number)
            break
        elif my_rate[i] > number > my_rate[i+1]:
            my_rate.insert(i+1, number)
            break
    print(my_rate)
