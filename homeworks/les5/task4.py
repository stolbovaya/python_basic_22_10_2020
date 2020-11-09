"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
from num2words import num2words

file_in = open('number_in.txt', 'r', encoding='UTF-8')
file_out = open('number_out.txt', 'w', encoding='UTF-8')
try:
    for line in file_in:
        el = list(filter(None, line.rstrip().split(' ')))
        el = num2words(int(el[2]), lang='ru') + ' - ' + el[2] + '\n'
        file_out.write(el)
except:
    print(f'Ошибка обработки')
finally:
    file_in.close()
    file_out.close()
