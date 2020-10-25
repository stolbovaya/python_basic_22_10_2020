"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

user_str = (input('введите целое положительное число\n >>>'))
idx = len(user_str)-1
user_int = int(user_str)
max_int = -1
while idx >= 0:
    cur_int = user_int // 10**idx
    if cur_int > max_int:
        max_int = cur_int
    user_int = user_int % 10**idx
    idx -= 1
print(f"максимальная цифра = {max_int}")

