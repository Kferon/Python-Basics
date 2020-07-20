class Matrix:
    def __init__(self, matrix1):
        matrix1 = ((list(input('Введите первую строчку через пробел: ').split()),
                    list(input('Введите вторую строчку через пробел: ').split())))
        self.matrix1 = matrix1

    def __add__(self, matrix2):

        matrix2 = ((list(input('Введите первую строчку через пробел: ').split()),
                    list(input('Введите вторую строчку через пробел: ').split())))
        self.matrix2 = matrix2
        my_answer = [[], []]

        for i in range(len(self.matrix1)):

            for j in range(len(self.matrix2[i])):
                my_answer[i].append(int(self.matrix1[i][j]) + int(self.matrix2[i][j]))

        return '\n'.join('\t'.join(str(j) for j in i) for i in my_answer)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, string)) for string in self.matrix1)


m1 = Matrix(0)
print(m1.__add__(0))
