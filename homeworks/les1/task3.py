"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
while True:
    user_int = input('введите целое число\n >>>')
    if user_int.isdigit():
        user_int = int(user_int)
        break
    print('Ошибка введено не число')
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
