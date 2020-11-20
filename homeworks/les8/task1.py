"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода.
 Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
 Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
  Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, date_str):
        self.__date_str = str(date_str)

    @classmethod
    def pars_date(cls, date_str):
        try:
            my_list = list(map(int, date_str.split('-')))
            my_dict = dict(day=my_list[0], month=my_list[1], year=my_list[2])
            if not cls.check_date(my_dict):
                raise TypeError(f'Не верное значение данных.')
        except ValueError as e:
            raise TypeError(f'{e}\nНе верное значение данных.')
        return my_dict

    @staticmethod
    def check_date(date_dict: dict):

        if date_dict['year'] < 0:
            return False
        if (date_dict['month'] > 12) or (date_dict['month'] < 1):
            return False
        leap_year = 0
        if date_dict['year'] % 4 == 0:
            leap_year = 1

        if (date_dict['day'] < 1) or (
                (date_dict['month'] in [1, 3, 5, 7, 8, 10, 12] and date_dict['day'] > 31) or (
                date_dict['month'] in [4, 6, 9, 11] and date_dict['day'] > 30) or (
                (date_dict['month'] == 2) and (date_dict['day'] > 28 + leap_year))):
            return False

        return True


if __name__ == '__main__':
    print(Date.pars_date("29-02-2020"))
    print(Date.pars_date("31-03-2020"))

    d1 = Date("29-02-2020")
    print(d1.pars_date("31-01-2020"))
