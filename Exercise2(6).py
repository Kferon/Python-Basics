class Road:
    _length = input('Введите длину дороги: ')
    _width = input('Введите ширину дороги: ')

    def road_height(self):
        check = '+'
        while check != 'q':
            try:
                height = int(self._width) * int(self._length) * 5 * 1
                print(f'Масса асфальта для покрытия данного дорожного полотна толщиной в 1 см: {height}т.')
            except ValueError:
                print('Введено не число')
            check = input('Для продолжения расчета нажмите любую клавишу кроме q: ')


x = Road()
x.road_height()

