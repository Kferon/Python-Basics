number = int(input('Введите целое положительное число'))
biggest = number % 10
number = number // 10
while number > 0:
    if biggest > number % 10:
        biggest = number % 10
        number = number // 10
    else:
        number = number // 10
print (biggest)
