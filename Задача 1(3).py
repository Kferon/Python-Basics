def numbers(x, y):

    try:
        number = x / y
        return number
    except ValueError:
        return 'Введено не число'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print(numbers(x=int(input('Введите делимое: ')), y=int(input('Введите делитель: '))))
