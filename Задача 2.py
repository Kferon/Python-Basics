my_list = list(input('Введите элементы списка через пробел: ').split())
my_list1 = []
i = 0
while (i + 1) < len(my_list):
    if i % 2 == 0:
        my_list1.append(my_list[i+1])
    else:
        my_list1.append(my_list[i-1])
    i = i+1
if len(my_list) % 2 == 1: my_list1.append(my_list[i])
print(my_list1)
