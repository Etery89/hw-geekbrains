"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно
— первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, list_row_from_matrix):
        self.list_from_matrix = list_row_from_matrix

    def __str__(self):
        elem_for_print = []
        for el in self.list_from_matrix:
            tmp_list = [str(num) for num in el]
            elem_for_print.append(tmp_list)
        return "{}\n{}".format(" ".join(elem_for_print[0]), " ".join(elem_for_print[1]))

    def __add__(self, other):
        new_matrix = []
        for num in range(len(self.list_from_matrix)):
            tmp_list = []
            for el1, el2 in zip(self.list_from_matrix[num], other.list_from_matrix[num]):
                tmp_list.append(el1 + el2)
            new_matrix.append(tmp_list)
        return Matrix(new_matrix)


list_1 = [[1, 2, 3, 6], [4, 5, 6, 7]]
list_2 = [[1, 1, 1, 1], [1, 1, 1, 1]]

matrix1 = Matrix(list_1)
matrix2 = Matrix(list_2)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
