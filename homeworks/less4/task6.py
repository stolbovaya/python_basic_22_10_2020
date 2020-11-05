"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
"""
from itertools import cycle


def my_cycle(iter_object):
    idx = 0
    len_iter = len(iter_object)
    while True:
        yield iter_object[idx]
        idx = idx + 1 if idx < len_iter else 0


def int_iter(n):
    while True:
        yield n
        n += 1


for itm in int_iter(15):
    print(itm)
    if itm > 20:
        break
