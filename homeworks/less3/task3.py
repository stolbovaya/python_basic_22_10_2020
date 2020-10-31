"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.

"""


def sum_max2(number1=0, number2=0, number3=0):
    """ Возвращает максимальную сумму 2-х чисел
    :param number1: 1 чесло
    :param number2: 2 чесло
    :param number3: 3 чесло
    :return:
    """
    return sum(max([number1, number2], [number1, number3], [number2, number3], key=sum))


input_list = []
max_number = 3
idx = 0
while idx < max_number:
    while True:
        user_value = input(f'Введите {idx + 1} число\n')
        try:
            value = int(user_value)
            break
        except ValueError as e:
            print(f"{e}\nНе верное значение данных")
            continue
    input_list.append(value)
    idx += 1

print(f'максимальная сумма 2-х чисел {sum_max2(input_list[0], input_list[1], input_list[2])}')
