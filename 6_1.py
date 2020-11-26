# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.
import time


class TrafficLight:
    _color = None
    _colors = ['red', 'yellow', 'green']

    def __init__(self, red, yellow, green):
        self.red = red
        self.yellow = yellow
        self.green = green

    def running(self):
        while True:
            print(f'\r red', end="")
            time.sleep(7)
            print(f'\r yellow', end="")
            time.sleep(2)
            print(f'\r green', end="")
            time.sleep(3)


traffic = TrafficLight('red', 'yellow', 'green')
traffic.running()
