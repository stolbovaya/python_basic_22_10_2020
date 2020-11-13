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


class Matrix:
    matrx = []

    def __init__(self, matrx):
        self.matrx = matrx

    def __str__(self):
        result = ''

        for el in self.matrx:
            result += " ".join(map(str, el)) + "\n"
        return result

    def __add__(self, other):
        cnt_r_1 = len(self.matrx)
        cnt_r_2 = len(other.matrx)
        idx_row = 0
        result_row = []
        while idx_row < min(cnt_r_1, cnt_r_2):
            cnt_c_1 = len(self.matrx[idx_row])
            cnt_c_2 = len(other.matrx[idx_row])
            idx_col = 0
            result_col = []
            while idx_col < min(cnt_c_1, cnt_c_2):
                result_col.append(self.matrx[idx_row][idx_col] + other.matrx[idx_row][idx_col])
                idx_col += 1
            while idx_col < max(cnt_c_1, cnt_c_2):
                if cnt_c_1 > cnt_c_2:
                    result_col.append(self.matrx[idx_row][idx_col])
                elif cnt_c_1 < cnt_c_2:
                    result_col.append(other.matrx[idx_row][idx_col])
                idx_col += 1
            result_row.append(result_col)
            idx_row += 1
        while idx_row < max(cnt_r_1, cnt_r_2):
            if cnt_r_1 > cnt_r_2:
                result_row.append(self.matrx[idx_row])
            elif cnt_r_1 < cnt_r_2:
                result_row.append(other.matrx[idx_row])
            idx_row += 1

        return result_row


matrix1 = Matrix([[1, 2], [2, 2], [3, 3]])
matrix2 = Matrix([[1, 1, 1], [2], [3, 3, 4, 5, 6], [7, 7]])
matrix = Matrix(matrix1 + matrix2)
print(matrix)
