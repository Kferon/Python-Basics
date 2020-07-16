class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return(f'{self.name} остановилась.')

    def turn(self, direction):
        return(f'{self.name} повернула {direction}.')

    def show_speed(self):
        return f'Скорость {self.name}: {self.speed} км/ч.'

    def police(self):
        if self.is_police:
            return('Эта машина принадлежит полиции')
        else:
            return('Эта машина не принадлежит полиции')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed} км/ч.')
        if int(self.speed) > 60:
            print('Вы превышаете максимальную скорость в 60 км/ч.')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name}: {self.speed} км/ч.')
        if int(self.speed) > 40:
            print('Вы превышаете максимальную скорость в 40 км/ч.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


a = Car(100, 'black', 'Mazda', False)
print(a.show_speed())
b = TownCar(70, 'white', 'Audi', False)
b.show_speed()
print(b.go())
c = WorkCar(20, 'Gray', 'BMV', False)
c.show_speed()
print(c.stop())
print(c.police())
d = PoliceCar(50, 'white', 'KIA', True)
print(d.police())
print(d.turn('налево'))
print(d.color)