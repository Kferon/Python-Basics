def my_func(x, y):
    i = 0
    answer = 1
    while i < abs(y):
        answer = 1/x * answer
        i += 1
    return answer

check = True
while check:
    try:
        print(my_func(x=int(input('Введите основание(целое положительное число): ')), y=int(input('Введите показатель(целое отрицательное число): '))))
        check = input('Для продолжения нажмите любую клавишу кроме q: ')
        if check == 'q':
            check = False
    except ValueError:
        print('Введено не число')
    except ZeroDivisionError:
        print('Основание не может быть равно нулю')