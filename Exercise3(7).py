class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return int(self.nucleus) + int(other.nucleus)

    def __sub__(self, other):
        return (int(self.nucleus) - int(other.nucleus)) if int(self.nucleus) > int(other.nucleus) else print(
            'Разница клеток отрицательна')

    def __mul__(self, other):
        return int(self.nucleus) * int(other.nucleus)

    def __truediv__(self, other):
        return int(self.nucleus) // int(other.nucleus)

    def make_order(self, nucleus_string):
        string = ''
        for i in range(int(self.nucleus // nucleus_string)):
            string += f'{"*" * nucleus_string}\n'
        string = string + '*' * (self.nucleus % nucleus_string)
        return string
x = Cell(5)
y = Cell(2)

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x.make_order(2))