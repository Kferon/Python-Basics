def my_func():
    sum = 0
    check = True
    while check:
        numbers = list(input('Введите ряд чисел через пробел(если хотите закончить, нажмите q): ').split())
        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                check = False
            else:
                sum = sum + int(numbers[i])
        print(sum)
my_func()
