"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
 Используйте форматирование строк.
"""

user_seconds = int(input('введите время в секундах\n >>>'))
hours = user_seconds // 3600
minutes = user_seconds % 3600 // 60
seconds = user_seconds % 60

print('{:02d}:{:02d}:{:02d}'.format(hours,minutes,seconds))

