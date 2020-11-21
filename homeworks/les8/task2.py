"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
"""


class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b) -> int:
    if b == 0:
        raise DivZero('')
    return a / b


try:
    result = div(10, 0)
except DivZero:
    result = float('inf')

print(result)
