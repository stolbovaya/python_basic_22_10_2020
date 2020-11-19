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
            self.__reshape(self.__shape[0])

    @property
    def shape(self):
        return self.__shape

    def __reshape(self, toLen):
        for itm in self.__array:
            tmp = toLen - len(itm)
            if tmp:
                itm.extend([0 for _ in range(tmp)])

    def __getitem__(self, item):
        return tuple(self.__array[item])

    def __iter__(self):
        return self.__array.__iter__()

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'This is Not Matrix this is {type(other).__name__}')
        # Складываем матрицы разных размерностей
        m1 = deepcopy(self)
        m2 = deepcopy(other)
        if m1.shape[1] > m2.shape[1]:
            m2.__array.extend([[0 for _ in range(m2.__shape[0])] for _ in range(m1.__shape[1] - m2.__shape[1])])
        else:
            m1.__array.extend([[0 for _ in range(m1.__shape[0])] for _ in range(m2.__shape[1] - m1.__shape[1])])

        if m1.shape[0] > m2.shape[0]:
            m2.__reshape(m1.__shape[0])
        else:
            m1.__reshape(m2.__shape[0])

        return Matrix(list(map(lambda y: list(map(sum, y)),
                               map(lambda x: list(zip(*x)), zip(m1, m2))
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
    matrix1 = Matrix([[1, 2, 1, 4], [2, 2], [3, 3]])
    print(matrix1)
    matrix2 = Matrix([[10, 1, 1], [2], [3, 3, 4], [5], [6]])
    print(matrix2)
    matrix = matrix1 + matrix2
    print('-----------------------------------------------------')
    print(matrix)
    print(matrix1)
    print(matrix2)
