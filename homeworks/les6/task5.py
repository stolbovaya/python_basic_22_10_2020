"""
5. Реализовать класс Stationery (канцелярская принадлежность).
 Определить в нем атрибут title (название) и метод draw (отрисовка).
 Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
  В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
 Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = ''

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def __init__(self, title='ручка'):
        super().__init__(title)

    def draw(self):
        print(f'Рисует {self.title}.')


class Pencil(Stationery):
    def __init__(self, title='карандаш'):
        super().__init__(title)

    def draw(self):
        print(f'Рисует {self.title}.')


class Handle(Stationery):
    def __init__(self, title='маркер'):
        super().__init__(title)

    def draw(self):
        print(f'Рисует {self.title}.')


pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle('красный маркер')
handle.draw()
