"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
 и строк и сохраните в переменные, выведите на экран.
"""

user_name = input('ваше имя\n >>>')
age = int(input('ваш возраст\n >>>'))
weight = float(input('ваш вес\n >>>'))

user_hello_string = f"Привет {user_name} твой возраст {age} твой вес {weight}"
print(user_hello_string)
