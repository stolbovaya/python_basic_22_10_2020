"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
 В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv

script_name, work_hours, rate_hour, bonus = argv
try:
    work_hours = int(work_hours)
    rate_hour= float(rate_hour)
    bonus = float(bonus)
    print(f"Заработная плата = {work_hours*rate_hour+bonus}")
except ValueError as e:
    print(f"{e}\nНе верное значение данных")

