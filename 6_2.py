# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.

class Road:
    # атрибуты класса
    __length = None
    __width = None
    weight = None
    layer = None

    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('Creat new_road object')

    def result(self):
        self.weight = 25
        self.layer = 0.05

        result = self.length * self.width * self.weight * self.layer / 1000
        print(f'Need {result} ton for the building')


new_road = Road(20000, 6)
new_road.result()
