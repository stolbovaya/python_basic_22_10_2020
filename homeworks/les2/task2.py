"""
2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
while True:
    count_elements = input('введите количество элемент в списке\n >>>')
    if count_elements.isdigit():
        count_elements = int(count_elements)
        break
    print(f"Ошибка введите число")

some_list = []
idx = 0
while idx < count_elements:
    some_list.append(input('введите элемент списка\n >>>'))
    idx += 1
print(f"Введенный список {some_list}")
idx = 0
while idx <= count_elements // 2:
    element = some_list[idx]
    some_list[idx] = some_list[idx+1]
    some_list[idx+1] = element
    idx += 2
print(f"Обработанный список {some_list}")
