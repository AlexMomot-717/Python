# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list_mtrx):
        self.list_mtrx = list_mtrx

    def __str__(self):
        for i in self.list_mtrx:
            for j in i:
                print(j,end=' ')
            print()
        return ''

    def __add__(self, other):
        for i in range(len(self.list_mtrx)):
            for j in range(len(self.list_mtrx[i])):
                self.list_mtrx[i][j] = self.list_mtrx[i][j] + other.list_mtrx[i][j]
        return Matrix.__str__(self)


mtrx_1 = Matrix([[1,2,3], [4,5,6], [7,8,9]])
print(mtrx_1)
mtrx_2 = Matrix([[9,8,7], [6,5,4], [3,2,1]])
print(mtrx_2)
print(mtrx_1 + mtrx_2)
