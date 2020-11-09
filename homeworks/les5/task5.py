"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

list_elements = [random.randint(1, 100) for _ in range(random.randint(100, 500))]

file_out = open('out.txt', 'w', encoding='UTF-8')
file_out.write(" ".join(map(str, list_elements)))
file_out.close()
print(list_elements)
print(sum(list_elements))

user_list = []
file_in = open('out.txt', 'r', encoding='UTF-8')
for line in file_in:
    user_list = map(int, line.split(' '))
file_in.close()
print(sum(user_list))
