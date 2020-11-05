"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
"""


def print_personal_info(name='', surname='', yaer_birthday='', city='', email='', phone=''):
    """ Распечатывет персональные данные

    :param name: имя
    :param surname: фамилия
    :param yaer_birthday: год рождения
    :param city: город проживания
    :param email: email
    :param phone: телефон
    :return:
    """
    print(f'{name} {surname} {yaer_birthday} {city} {email} {phone}')


input_template = {
    'имя': str,
    'фамилия': str,
    'год рождения': str,
    'город проживания': str,
    'email': str,
    'телефон': str
}

input_dict = {}
for key, value in input_template.items():
    while True:
        user_value = input(f'{key}\n')
        try:
            value = user_value
            break
        except ValueError as e:
            print(f"{e}\nНе верное значение данных")
            continue
    input_dict[key] = value

print(input_dict)
print_personal_info(phone=input_dict['телефон'], city=input_dict['город проживания'], name=input_dict['имя'],
                    surname=input_dict['фамилия'],
                    yaer_birthday=input_dict['год рождения'], email=input_dict['email'])
