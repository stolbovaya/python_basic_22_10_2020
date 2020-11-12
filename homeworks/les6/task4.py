"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
 Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
 Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
 должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('START')

    def stop(self):
        print('STOP')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(direction)
        else:
            print('direction must be left or right')

    def show_speed(self):
        print(self.speed)

    def show_name(self):
        print(self.name)


class TownCar(Car):
    def __init__(self, speed, color, name='TownCar'):
        super().__init__(speed, color, name, False)


def show_speed(self):
    print(self.speed)
    if self.speed > 60:
        print('Скорость превышина')


class SportCar(Car):
    def __init__(self, speed, color, name='SportCar'):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name='WorkCar'):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Скорость превышина')


class PoliceCar(Car):
    def __init__(self, speed, color, name='PoliceCar'):
        super().__init__(speed, color, name, True)


car = Car(70, 'Red', 'Машина', False)
car.show_name()
car.go()
car.turn('left')
car.show_speed()
car.stop()
print('')
workCar = WorkCar(70, 'White')
workCar.show_name()
workCar.show_speed()

print('')
townCar = TownCar(60, 'Green', 'Машина')
townCar.show_name()
townCar.show_speed()
print('')

policeCar = PoliceCar(160, 'Red')
policeCar.show_name()
policeCar.go()
policeCar.turn('dddd')
policeCar.show_speed()
policeCar.stop()
print('')

car = SportCar(160, 'Red')
car.show_name()
car.go()
car.turn('left')
car.show_speed()
car.stop()
