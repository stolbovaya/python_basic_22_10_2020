"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""
user_list = [1, 2, 2, 3, 3, 6, 8, 9, 4, 56, 1, 8, 9]
print(user_list)
result_list = []
itm_before = user_list[0]
for itm in user_list:
    if itm > itm_before:
        result_list.append(itm)
    itm_before = itm
print(result_list)
