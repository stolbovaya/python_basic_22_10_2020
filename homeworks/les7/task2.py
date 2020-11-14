"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    def __init__(self, height, name='пальто'):
        self.name = name
        self.height = height

    @property
    def expense(self):
        return self.height / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, size, name='костюм'):
        self.name = name
        self.size = size

    @property
    def expense(self):
        return 2 * self.size + 0.3


coat = Coat( 179)
print(coat.expense)
suit = Suit( 10)
print(suit.expense)
print(f'Общий расход ткани = {coat.expense + suit.expense}')
