check = 'Да'
number = 1
my_list = []
name = []
price = []
quantity = []
si = []
while check == 'Да' or check == '+' or check == 'да' or check == 'yes' or check == 'Yes':
    my_dict = dict({'Название: ': input('Название: '), 'Цена: ': input('Цена: '), 'Количество: ': input('Количество: '), 'Единица измерения: ': input('Единица измерения: ')})
    my_list.append((number, my_dict))
    number += 1
    check = input('Хотите ли вы добавить еще один товар? ')
    x = my_dict.get('Название: ')
    y = my_dict.get('Цена: ')
    z =my_dict.get('Количество: ')
    b = my_dict.get('Единица измерения: ')
    name.append(x)
    price.append(y)
    quantity.append(z)
    si.append(b)
    analysis = dict({'Названия: ': name, 'Цены: ': price, 'Количества: ': quantity, 'Единицы измерения: ': si})
print(my_list)
print(analysis)