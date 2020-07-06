def int_func(word):
    word1 = word.title()
    return word1


print(int_func(word=input('Введите слово из маленьких латинских букв: ')))


result = []
my_list = list(input('Введите список слов из маленьких латинских букв через пробел: ').split())
for i in range(len(my_list)):
    result.append(int_func(my_list[i]))
print(result)

