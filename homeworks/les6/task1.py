"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
from time import sleep


class TrafficLight:
    _time_light = {}

    def __init__(self, time_red=7, time_yellow=2, time_green=10):
        self._time_light = {"красный": time_red, "желтый": time_yellow, "зеленый": time_green}

    def running(self):
        idx = 0
        while idx < 10:
            for key, time in self._time_light.items():
                print(key)
                sleep(time)
            idx += 1


trafficLight = TrafficLight(1, 1, 1)
trafficLight.running()
