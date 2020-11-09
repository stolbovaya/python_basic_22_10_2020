"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

file = open('income.txt', 'r', encoding='UTF-8')

idx = 0
user_list = []
res_list = []
for line in file:
    res_list.append((list(filter(None, line.rstrip().split(' ')))))  # Убираем лишние пробелы
file.close()

print(res_list)
user_sum = 0
user_count = 0
status_job = True
for el in res_list:
    try:
        el[1] = int(el[1])
    except ValueError as e:
        print(f"{e}\nНе верное значение данных")
        status_job = False
        break

    user_sum += el[1]
    user_count += 1
    if el[1] < 20000:
        print(el[0])

if (user_count > 0) and (status_job):
    print(f'Средния величина дохода сотрудников = {user_sum / user_count}')
else:
    print(f'В файле отсутствуют данны или данные неверного формата.')
