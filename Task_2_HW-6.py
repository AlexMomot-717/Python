# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для
# покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв м. дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:

    def __init__(self, _lenght, _width):
        self._length = _lenght
        self._width = _width
        # self.relative_weight = 25
        # self.height = 5

    def get_asphalt_mass(self):
        relative_weight = 25
        height = 5
        asphalt_mass = int(self._length * self._width * relative_weight * height / 1000)
        return f"Asphalt mass for {self._length}(m)x{self._width}(m) road: {asphalt_mass} tons"


r15 = Road(160000, 8)
print(r15.get_asphalt_mass())
