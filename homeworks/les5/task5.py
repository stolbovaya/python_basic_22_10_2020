"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
import random

list_elements = [str(random.randint(1, 100)) for itm in range(1, 1001)]

file_out = open('out.txt', 'w', encoding='UTF-8')
file_out.write(" ".join(list_elements))
file_out.close()

user_list =[]
file_in = open('out.txt', 'r', encoding='UTF-8')
user_str = file_in.readlines()
user_list=user_str.split(' ')
file_in.close()

print(list_elements)
print(user_list)
