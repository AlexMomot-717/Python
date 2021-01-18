# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).  А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} goes.')

    def stop(self):
        print(f'{self.name} stops.')

    def turn(self, direction):
        print(f'{self.name} turns {direction}.')

    def show_speed(self):
        print(f'{self.name} goes with speed {self.speed}.')


class TownCar(Car):

    def show_speed(self):
        speed_limit = 60
        if self.speed <= speed_limit:
            print(f'{self.name} goes with speed {self.speed}.')
        else:
            print(f'{self.name} goes with speed {self.speed}. Slow down! Speed limit is {speed_limit}.')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        speed_limit = 40
        if self.speed <= speed_limit:
            print(f'{self.name} goes with speed {self.speed}.')
        else:
            print(f'{self.name} goes with speed {self.speed}. Slow down! Speed limit is {speed_limit}.')


class PoliceCar(Car):
    pass

print()

car_1 = PoliceCar(80, 'grey', 'Lada Priora', True)
print(f'car_1 info: name {car_1.name}, color {car_1.color}, current speed {car_1.speed}, police car - {car_1.is_police}')
car_1.go()
car_1.turn('left')
car_1.show_speed()
car_1.stop()
print()

car_2 = WorkCar(50, 'orange', 'КАМАЗ', False)
print(f'car_2 info: name {car_2.name}, color {car_2.color}, current speed {car_2.speed}, police car - {car_2.is_police}')
car_2.go()
car_2.turn('right')
car_2.show_speed()
car_2.stop()
print()

car_3 = SportCar(220, 'blue', 'Bugatti Veyron', False)
print(f'car_3 info: name {car_3.name}, color {car_3.color}, current speed {car_3.speed}, police car - {car_3.is_police}')
car_3.go()
car_3.turn('right')
car_3.show_speed()
car_3.stop()
print()

car_4 = TownCar(70, 'yellow', 'Hyundai i20', False)
print(f'car_4 info: name {car_4.name}, color {car_4.color}, current speed {car_4.speed}, police car - {car_4.is_police}')
car_4.go()
car_4.turn('left')
car_4.show_speed()
car_4.stop()
print()