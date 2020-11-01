"""
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
 но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(word=''):
    return word[:1].upper() + word[1:]


user_list = input('введите строку из нескольких слов, разделённых пробелами\n >>>')
user_list = user_list.split(' ')

user_list = list(map(int_func,user_list))
user_str = ' '.join(user_list)
print(f'{user_str}')
