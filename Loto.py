import random
import copy
import time


class Loto:

    def __init__(self, my_list, string_1, string_2, name_1, name_2):
        self.my_list = my_list
        self.string_1 = string_1
        self.string_2 = string_2
        self.name_1 = name_1
        self.name_2 = name_2

    def generation(self):
        nothing = list('  ' * 4)
        self.my_list = []
        self.string_1 = []
        print(f'------ Карточка {self.name_1} -----')
        for n in range(3):
            numbers = []

            for i in range(1, 6):
                num = random.randint(1, 90)
                self.my_list.append(num)
                numbers.append(' ' + str(num) + ' ')

            numbers = numbers
            card = nothing + numbers
            random.shuffle(card)
            self.string_1.append(card)
            print(''.join(card))
        print('--------------------------')
        self.my_list = []
        self.string_2 = []
        print(f'------ Карточка {self.name_2} -----')
        for n in range(3):
            numbers = []

            for i in range(1, 6):
                num = random.randint(1, 90)
                self.my_list.append(num)
                numbers.append(' ' + str(num) + ' ')

            numbers = numbers
            card = nothing + numbers
            random.shuffle(card)
            self.string_2.append(card)
            print(''.join(card))
        print('--------------------------')

    def game(self):
        b = 0
        el = 0
        my_random = []
        lol = []
        for i in range(91):
            my_random.append(i)
        while el <= 1000:
            game_num = random.randint(1, 90)
            for i in my_random:
                if game_num == i:
                    my_random.remove(game_num)
                    print(f'New random number: {game_num}')
                    lol.append(game_num)
                    break
                else:
                    continue

            check = input('Press y do delete number, n to stay: ')
            if check == 'y':
                answer = copy.deepcopy(self.string_1)
                for i in range(3):
                    for j in range(12):
                        try:
                            if int(self.string_1[i][j]) == game_num:
                                self.string_1[i].pop(j)
                                self.string_1[i].insert(j, ' - ')
                        except ValueError:
                            continue
                print(f'------ Карточка {self.name_1} -----')
                for l in range(3):
                    print(''.join((self.string_1[l])))
                if self.string_1 == answer:
                    print('(ಥ﹏ಥ) You lose! (ಥ﹏ಥ)')
                    time.sleep(5000)

            else:
                answer = copy.deepcopy(self.string_1)
                for i in range(3):
                    for j in range(12):
                        try:
                            if int(self.string_1[i][j]) == game_num:
                                self.string_1[i].pop(j)
                                self.string_1[i].insert(j, ' - ')
                        except ValueError:
                            continue
                print(f'------ Карточка {self.name_1} -----')
                for l in range(3):
                    print(''.join((self.string_1[l])))
                if self.string_1 != answer:
                    print('(ಥ﹏ಥ) You lose! (ಥ﹏ಥ)')
                    time.sleep(5000)
            print('--------------------------')
            print(f'------ Карточка {self.name_2} -----')
            for i in range(3):
                for j in range(12):
                    try:
                        if int(self.string_2[i][j]) == game_num:
                            self.string_2[i].pop(j)
                            self.string_2[i].insert(j, ' - ')
                    except ValueError:
                        continue
            for l in range(3):
                print(''.join((self.string_2[l])))
            print('--------------------------')

            for i in range(3):
                for j in range(12):
                    if self.string_2[i][j] ==' - ':
                        b += 1
                    if b == 15:
                        print('(ಥ﹏ಥ) You lose! (ಥ﹏ಥ)')
                        time.sleep(3000)
                    else:
                        b = 0


            for i in range(3):
                for j in range(12):
                    if self.string_1[i][j] ==' - ':
                        b += 1
                    if b == 15:
                        print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ You win! ✧ﾟ･: *ヽ(◕ヮ◕ヽ)')
                        time.sleep(3000)
                    else:
                        b = 0


            el += 1
        # print(my_random)
        # print(check)


x = Loto(0, [], [], input('Введите свое имя: '), 'Computer')

x.generation()
x.game()
# print(x.string[0])
# print(''.join(x.string[0]))
