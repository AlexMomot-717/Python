#  Реализовать класс Stationery (канцелярская принадлежность).
#  Определить в нем атрибут title (название) и метод draw (отрисовка).
#  Метод выводит сообщение “Запуск отрисовки.”
#  Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
#  В каждом из классов реализовать переопределение метода draw.
#  Для каждого из классов методы должен выводить уникальное сообщение.
#  Создать экземпляры классов и проверить,
#  что выведет описанный метод для каждого экземпляра.

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):

    def draw(self):
        print('Выполнение эскиза.')


class Pencil(Stationary):
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Создание рисунка.')


class Handle(Stationary):
    def __init__(self, title):
        self.title = title

    def draw(self):
        super().draw()  # тест на родительский метод
        print('Создание жирных линий.')


d_1 = Stationary('paint_brush')
d_1.draw()

d_2 = Pen('black_color_pen')
d_2.draw()

d_3 = Pencil('green_color_pencil')
d_3.draw()

d_4 = Handle('yellow_color_handle')
d_4.draw()
