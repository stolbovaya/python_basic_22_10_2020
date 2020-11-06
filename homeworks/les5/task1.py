"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

file = open('user.txt', 'w', encoding='UTF-8')
while True:
    str_input = input('Введите строку \n>>>')
    if str_input > '':
        file.write(str_input + '\n')
    else:
        break
file.close()
