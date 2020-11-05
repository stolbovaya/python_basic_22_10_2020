"""
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
"""
from functools import reduce


def multiply_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el


res = [itm for itm in range(100, 1001) if itm % 2 == 0]
print(reduce(multiply_func, res))
