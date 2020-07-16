class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        x = sum(self._income.values())
        print(x)


a = Position('Ivan', 'Ivanov', 'Manager', 90000, 15000)
a.get_full_name()
a.get_total_income()
print(a.position)
