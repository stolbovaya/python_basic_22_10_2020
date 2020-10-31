"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def division_func(p_1=0, p_2=1):
    """Возвращает частное от деления.

    Именованные параметры:
    p_1 -- делимое (по умолчанию 0.0)
    p_2 -- делитель (по умолчанию 1.0)

    """
    if p_2 == 0:
        print('Ошибка деление на ноль. ')
        return None     # пишем в явном виде для читаемости кода
    else:
        return p_1 / p_2


input_template = {
    'делимое': int,
    'делитель': int
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

print(f'Частное = {division_func(input_dict["делимое"],input_dict["делитель"])}')

