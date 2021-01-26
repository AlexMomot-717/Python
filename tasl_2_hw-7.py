# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
from math import ceil

class Clothes(ABC):
    def __init__(self, size, height):
        self.s = size
        self.h = height

    @property
    def consumption(self):
        return f'Общий расход ткани: {ceil(self.s / 6.5 + 0.5 + 2 * self.h + 0.3)} метров'


class Coat(Clothes):
    def __init__(self, size):
        self.s = size

    @property
    def consumption(self):
        return f'Для пошива пальто требуется: {ceil(self.s / 6.5 + 0.5)} метров ткани'


class Suit(Clothes):
    def __init__(self, height):
        self.h = height

    @property
    def consumption(self):
        return f'Для пошива костюма требуется: {ceil(2 * self.h + 0.3)} метров ткани'

suit_1 = Suit(1.85)
print(suit_1.consumption)

coat_1 = Coat(46)
print(coat_1.consumption)

print(Clothes(46, 1.85).consumption)
