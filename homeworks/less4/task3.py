"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
import random

user_list = [20, 20, 240, 24, 56, 87, 95, 74, 85, 21, 45, 42]
result_list = [itm for itm in user_list if ((itm % 20 == 0) or (itm % 21 == 0))]
print(user_list)
print(result_list)
