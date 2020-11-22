"""
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение
и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class Complex:

    def __init__(self, a: int, b: int):
        self.__a = int(a)
        self.__b = int(b)

    def __add__(self, other):
        return Complex(self.__a + other.__a, self.__b + other.__b)

    def __sub__(self, other):
        return Complex(self.__a - other.__a, self.__b - other.__b)

    def __str__(self):
        return f'{self.__a}+{self.__b}i'


if __name__ == '__main__':
    complex1 = Complex(10, 3)
    complex2 = Complex(20, 5)
    print(f'{complex1} + {complex2} = {complex1 + complex2}')
    print(f'({complex1}) - ({complex2}) = {complex1 - complex2}')
