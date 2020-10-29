"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
while True:
    user_int = input('введите целое число\n >>>')
    if user_int.isdigit():
        user_int = int(user_int)
        break
    print('Ошибка введено не число')

count = 0
user_count = user_int
while user_count:
    user_count //= 10
    count += 1

idx = count - 1
max_int = 0

while idx >= 0 and max_int != 9:
    cur_int = user_int // 10**idx
    if cur_int > max_int:
        max_int = cur_int
    user_int %= 10**idx
    idx -= 1

print(f"максимальная цифра = {max_int}")

