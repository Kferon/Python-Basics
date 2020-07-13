with open('file1.txt', 'r') as my_f:
    content = my_f.readlines()
    print(f'Количество строк: {len(content)}')
my_f = open('file1.txt', 'r')
i = 0
for string in my_f:
    check = 0
    x = 0
    i+=1
    for word in string:
        if word != ' ' and check == 0:
            x += 1
            check = 1
        elif word == ' ':
            check = 0
    print(f'Количество слов в {i} строке: {x}')