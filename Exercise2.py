
my_list = list(map(int, input('Введите числа через пробел: ').split()))
result = [my_list[i] for i in range(1,len(my_list)) if my_list[i] > my_list[i-1]]
print(result)