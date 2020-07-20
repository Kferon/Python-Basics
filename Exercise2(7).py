from abc import ABC, abstractmethod


class MyAbsClass(ABC):
    def qwasd(self):
        pass

    @abstractmethod
    def get_size(self):
        '''Получает размер для пальто и вычисляет общую площадь ткани'''
        pass

    @abstractmethod
    def get_height(self):
        '''Получает рост для пиджака и вычисляет общую площадь ткани'''
        pass


class Clothes(MyAbsClass):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    def get_size(self):
        return int(self.size) / 6.5 + 0.5

    def get_height(self):
        return int(self.height) * 2 + 0.3

    @property
    def get_all(self):
        if self.size == 0:
            return self.height * 2 + 0.3
        elif self.height == 0:
            return self.size / 6.5 + 0.5
        else:
            return self.size * 2 + self.height / 6.5 + 0.8


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def get_height(self):
        return 'Для пальто используется только характеристика размера'

    def get_size(self):
        return int(self.size) / 6.5 + 0.5

    @property
    def get_all(self):
        if self.size == 0:
            return self.height * 2 + 0.3
        elif self.height == 0:
            return self.size / 6.5 + 0.5
        else:
            return self.size / 6.5 + self.height * 2 + 0.8


class Blazer(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)

    def get_size(self):
        return 'Для пиджака используется только характеристика роста'

    def get_height(self):
        return int(self.height) * 2 + 0.3

    @property
    def get_all(self):
        if self.size == 0:
            return self.height * 2 + 0.3
        elif self.height == 0:
            return self.size / 6.5 + 0.5
        else:
            return self.size * 2 + self.height / 6.5 + 0.8


# x = Clothes(1, 2)
x = Blazer(0, 1)
print(x.get_size())
print(x.get_all)
print(x.get_height())

y = Coat(1, 0)
print(y.get_size())
print(y.get_all)
print(y.get_height())

z = Clothes(1, 1)
print(z.get_size())
print(z.get_all)
print(z.get_height())
