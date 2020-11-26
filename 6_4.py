# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police=True):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self):
        print(f'{self.name} повернула')

    def show_speed(self):
        print(f'{self.name} едет со скоростью{self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} превышает скорость')
            print(f'{self.name} едет со скоростью {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} превышает скорость')
            print(f'{self.name} едет со скоростью {self.speed}')


class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print(f'{self.name} полиция')


car_1 = TownCar(80, 'красная', 'Маруся')
car_1.go()
car_1.show_speed()
car_1 = WorkCar(50, 'желтый', 'Газель')
car_1.stop()
car_1.show_speed()
car_1 = SportCar(250, 'белый','Запорожец')
car_1.turn()
car_1 = PoliceCar(10, 'синий', 'УАЗ', True)
car_1.police()
car_1.turn()

