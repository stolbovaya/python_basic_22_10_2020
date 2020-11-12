"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
 В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
 Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов,
вызвать методы экземпляров).
"""


class Worker:
    _name = ''
    _surname = ''
    _position = ''
    __income = {"wage": 0, "bonus": 0}

    def __init__(self, name='', surname='', position='', income=0):
        self._name = name
        self._surname = surname
        self._position = position
        self.__income = income


class Position(Worker):
    def __init__(self, name='', surname='', position='', income=0, wage=0, bonus=0):
        self._Worker__income["wage"] = wage
        self._Worker__income["bonus"] = bonus
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self._name + ' ' + self._surname

    def get_total_income(self):
        return sum(self.__income[1])


staf = Position('Екатерина', 'Столбовая', 'ИТ-Архитектор', 5000, 1000)
print({staf.get_full_name})
print(staf.get_total_income)
