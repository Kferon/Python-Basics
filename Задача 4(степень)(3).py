def my_func(x, y):
    answer = 1 / x ** abs(y)
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