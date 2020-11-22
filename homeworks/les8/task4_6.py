"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
 Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.

"""
import sys
import os

sys.path.append(os.path.abspath("C://!Projects/python_basic_22_10_2020/homeworks/les8/"))

from task3 import *


class Storage:
    def __init__(self, name):
        self.__name = name
        self.__count_equipment = {}

    def __str__(self):
        rez = f'{self.get_name} :\n'

        for el in self.__count_equipment:
            rez += f'{el} - {self.get_count(el)} \n'

        return rez

    def add_storage(self, equipment, count=1):
        try:
            self.__count_equipment[equipment.get_type] = self.get_count(equipment.get_type) + to_int(count)
        except IntError:
            print(f'Ошибка! Введенный элемент не является числом.')

    @staticmethod
    def moving_storage(from_storage, to_storage, equipment, count):
        try:
            if from_storage.get_count(equipment.get_type) - to_int(count) > 0:
                from_storage.__count_equipment[equipment.get_type] = from_storage.get_count(equipment.get_type) - count
                to_storage.add_storage(equipment, count)
            else:
                print(
                    f'Оборудование "{equipment.get_type}" в количестве {count} отсутстует на складе.\n'
                    f'Остаток оборудования "{equipment.get_type}" '
                    f'- {from_storage.__count_equipment[equipment.get_type]}')
        except IntError:
            print(f'Ошибка! Введенный элемент не является числом.')

    def get_count(self, in_type) -> int:
        if self.__count_equipment.get(in_type):
            return self.__count_equipment.get(in_type)
        else:
            return 0

    @property
    def get_name(self):
        return self.__name


class OfficeEquipment:
    def __init__(self, type_eq, model, serial_number, cost=0):
        self.__type_eq = type_eq
        self.__model = model
        self.__serial_number = serial_number
        self.__cost = cost

    def __str__(self):
        return f'{self.__type_eq}'

    @property
    def get_type(self):
        return self.__type_eq


class Printer(OfficeEquipment):
    def __init__(self, model, serial_number, cost, model_cartridge):
        self.__model_cartridge = model_cartridge
        super().__init__('принтер', model, serial_number, cost)


class Scanner(OfficeEquipment):
    def __init__(self, model, serial_number, cost, is_color):
        self.__is_color = is_color
        super().__init__('сканер', model, serial_number, cost)


class Xerox(OfficeEquipment):
    def __init__(self, model, serial_number, cost, auto_feed):
        self.__auto_feed = auto_feed
        super().__init__('ксерокс', model, serial_number, cost)


if __name__ == '__main__':
    p1 = Printer('HP-1000', 'h21321321', 1000, 'H-333')
    p2 = Printer('HP-3565', 'h2367568', 2000, 'H-333')
    s1 = Scanner('HP-442', 's3423455', 3000, True)
    x1 = Xerox('Xerox-23', 'x32424234', 5000, True)

    storage1 = Storage('склад 1')
    department = Storage('Отдел продаж')

    storage1.add_storage(p1)
    storage1.add_storage(p2, 10)
    storage1.add_storage(s1, 10)
    storage1.add_storage(x1, 10)
    storage1.moving_storage(storage1, department, p1, 'dfs')
    storage1.moving_storage(storage1, department, x1, 5)

    print(storage1)
    print(department)
    storage1.moving_storage(storage1, department, x1, 10)
