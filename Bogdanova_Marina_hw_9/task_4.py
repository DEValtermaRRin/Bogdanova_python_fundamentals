# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    is_police = False

    def __init__(self, speed, name, color=None):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f'{self.color} {self.name} выехала')
        self.speed = 10

    def stop(self):
        print(f'{self.color} {self.name} остановилась')
        self.speed = 0

    def set_speed(self, new_speed):
        self.speed = new_speed

    def turn(self, direction=None):
        if direction == 'left':
            print(f'{self.color} {self.name} повернула налево')
        elif direction == 'right':
            print(f'{self.color} {self.name} повернула направо')
        else:
            print(f'{self.color} {self.name} поехала прямо')

    def show_speed(self):
        print(f'{self.color} {self.name}. Текущая скорость: {self.speed} км/ч')


class TownCar(Car):

    def show_speed(self):
        print(f'{self.color} {self.name}. Текущая скорость: {self.speed} км/ч')
        if self.speed > 60:
            print(f'{self.color} {self.name} превысила скорость!')
            PoliceCar.go(PoliceCar(self, 'Полицейская машина', ''))


class SportCar(Car):

    def show_speed(self):
        print(f'{self.color} {self.name}. Текущая скорость: {self.speed} км/ч')
        if self.speed > 130:
            print(f'{self.color} {self.name} превысила скорость!')
            PoliceCar.go(PoliceCar(self, 'Полицейская машина', ''))


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.color} {self.name}. Текущая скорость: {self.speed} км/ч')
        if self.speed > 40:
            print(f'{self.color} {self.name} превысила скорость!')
            PoliceCar.go(PoliceCar(self, 'Полицейская машина', ''))


class PoliceCar(Car):
    is_police = True

    def show_speed(self):
        print(f'{self.color} {self.name}. Текущая скорость: {self.speed} км/ч')
        if self.speed > 130:
            print(f'{self.color} {self.name} догоняет нарушителя')


police_car_1 = PoliceCar(65, 'Полицейская машина', '')
car_1 = TownCar(60, 'зеленая', 'Волга')
car_1.show_speed()
car_2 = SportCar(160, 'красная', 'BMW')
car_2.show_speed()
car_2.set_speed(60)
car_2.turn('right')
car_2.stop()
car_2.show_speed()
car_3 = WorkCar(50, 'синяя', 'Lada')
car_3.go()
car_3.set_speed(80)
car_3.show_speed()
car_3.stop()
police_car_1.set_speed(160)
police_car_1.show_speed()
