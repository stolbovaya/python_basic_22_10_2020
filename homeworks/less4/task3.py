"""
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
"""
import random
user_list = [el for el in range(random.randint(20, 240))]
result_list = [itm for itm in user_list if not ((itm % 20) or (itm % 21))]
print(user_list)
print(result_list)