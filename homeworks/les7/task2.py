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


class Clothes:
    def __init__(self, name):
        self.name = name


class Coat(Clothes):
    def __init__(self, name, height):
        self.height = height
        super().__init__(name)

    @property
    def expense(self):
        return self.height / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, name, size):
        self.size = size
        super().__init__(name)

    @property
    def expense(self):
        return 2 * self.size + 0.3


coat = Coat('пальто', 179)
print(coat.expense)
suit = Suit('костюм', 10)
print(suit.expense)
print(f'Общий расход ткани = {coat.expense + suit.expense}')
