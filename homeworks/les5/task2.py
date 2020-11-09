"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
 количества слов в каждой строке.
"""

file = open('user.txt', 'r', encoding='UTF-8')

idx = 0
user_dict = {}
for line in file:
    idx += 1
    user_dict[idx] = len(list(filter(None, line.rstrip().split(' '))))  # Пробел не считаем словом
file.close()
print(f'Количество строк = {idx}')
print(f'Количество слов по строкам: \n {user_dict}')
