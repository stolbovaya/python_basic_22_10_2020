"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""

user_int = int(input('введите целое число\n >>>'))
result = 0
idx = 0
idx_max = 3
count = 0
user_count = user_int

while user_count:
    user_count //= 10
    count += 1

while idx < idx_max:
    result += (idx_max-idx)*10**(idx*count)*user_int
    idx += 1
print(f"сумма чисел = {result}")
