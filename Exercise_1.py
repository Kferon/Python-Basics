my_list = []
with open('file0', 'w+') as my_f:
    while True:
        line = input('Введите строку: ')
        my_list.append(line+'\n')
        if line == '':
            break
    my_f.writelines(my_list)
my_f = open("file0", "r")
content = my_f.read()
print(content)
my_f.close()