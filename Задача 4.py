i = 0
number = 1
my_list = list(input('Введите строку из нескольких слов: ').split())
while i < len(my_list):
    print(number, (my_list[i][0:10]))
    i = i + 1
    number = number + 1
