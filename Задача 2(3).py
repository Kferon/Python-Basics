def information(name='Ivan', surname='Ivanov', birth_year='1999', town='Moscow', email='ivan@mail.ru',
                phone_number='8-800-555-35-35'):
    my_dict = {'Имя:': name, 'Фамилия:': surname, 'Год рождения:': birth_year, 'Город проживания:': town, 'email:': email, 'Номер телефона:': phone_number}
    return my_dict


print(information(name=input('Введите имя: '), surname=input('Введите фамилию: '), town = input('Введите город проживания: '), birth_year=input('Введите год рождения: '),
            email=input('Введите email: '), phone_number=input('Введите номер телефона: ')))
