def my_func(x, y, z):
    numbers = [x, y, z]
    numbers.remove(min(x, y, z))
    sum = int(numbers[0]) + int(numbers[1])
    return sum
check = True
while check:
    try:
        print(my_func(x=int(input('Введите 1-е число: ')), y=int(input('Введите 2-е число: ')), z=int(input('Введите 3-е число: '))))
        check = input('Для продолжения нажмите любую клавишу кроме q: ')
        if check == 'q':
            check = False
    except ValueError:
        print('Введено не число')
