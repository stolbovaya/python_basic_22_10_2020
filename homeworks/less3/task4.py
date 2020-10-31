"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""


def degree(x=0, y=0):
    return x ** y


def degree_cycle(x=0, y=0):
    idx = 1
    if y >= 0:
        result = x
    else:
        result = 1/x
    while idx < abs(y):
        if y >= 0:
            result *= x
        else:
            result /= x
        idx += 1
    return result


input_template = {
    'число x': int,
    'число y': int
}

input_dict = {}
for key, value in input_template.items():
    while True:
        user_value = input(f'{key}\n')
        try:
            value = int(user_value)
            break
        except ValueError as e:
            print(f"{e}\nНе верное значение данных")
            continue
    input_dict[key] = value
print(f'{input_dict["число x"]} в степени {input_dict["число y"]} = {degree(input_dict["число x"], input_dict["число y"])}')
print(f'{input_dict["число x"]} в степени {input_dict["число y"]} = {degree_cycle(input_dict["число x"], input_dict["число y"])}')
