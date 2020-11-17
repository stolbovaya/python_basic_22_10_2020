"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix(двух матриц).
 Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
from copy import deepcopy


class Matrix:

    def __init__(self, array: list):
        self.__array = deepcopy(array)
        self.__shape = (len(max(self.__array, key=len)), len(self.__array))
        if len(min(self.__array, key=len)) != self.shape[0]:
            self.__reshape()

    @property
    def shape(self):
        return self.__shape

    def __reshape(self):
        for itm in self.__array:
            tmp = self.shape[0] - len(itm)
            if tmp:
                itm.extend([0 for _ in range(tmp)])

    def __getitem__(self, item):
        return tuple(self.__array[item])

    def __iter__(self):
        return self.__array.__iter__()

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'This is Not Matrix this is {type(other).__name__}')
        if self.shape != other.shape:
            raise ValueError(f'Not equal shape matrix {self.shape} and {other.shape}')

        return Matrix(list(map(lambda y: list(map(sum, y)),
                               map(lambda x: list(zip(*x)), zip(self, other))
                               )
                           )
                      )

    def __str__(self):

        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.__array)))) + 1
        if not max_len_itm & 1:
            max_len_itm += 1

        result = ''
        for line in self.__array:
            result += ''.join([f'{itm:^{max_len_itm}}' for itm in line]) + '\n'
        return result


if __name__ == '__main__':
    matrix1 = Matrix([[1, 2, 1], [2, 2], [3, 3]])
    print(matrix1)
    matrix2 = Matrix([[10, 1, 1], [2], [3, 3, 4]])
    print(matrix2)
    matrix = matrix1 + matrix2
    print(matrix)
