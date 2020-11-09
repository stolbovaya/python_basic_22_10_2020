"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json

firms_dict = {}
firms_list = []
firms_count = 0
firms_sum_profit = 0

file_in = open('FirmsProfit.txt', 'r', encoding='UTF-8')
for line in file_in:
    el = (list(filter(None, line.rstrip().split(' '))))
    print(el)
    try:
        profit = int(el[2]) - int(el[3])
    except ValueError as e:
        print(f"{e}\nНе верное значение данных")
        continue
    firms_dict[el[0]] = profit

    if profit > 0:
        firms_sum_profit += profit
        firms_count += 1

file_in.close()
if firms_count > 0:
    average_profit = firms_sum_profit / firms_count
else:
    average_profit = float('inf')
firms_list = [firms_dict, dict(average_profit=average_profit)]
print(firms_list)

with open("FirmsProfit.json", "w") as write_file:
    json.dump(firms_list, write_file)
