# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return f"Full name of employee on position {self.position} : {full_name}"

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return f"{self.position}, {self.name} {self.surname}'s total income : {total_income}"


pos_1 = Position('Mark', 'Ginsburg', 'welder', 1000, 300)
print(pos_1.get_full_name())
print(pos_1.get_total_income())

pos_2 = Position('Fred', 'MacNill', 'mechanic', 900, 150)
print(pos_2.get_full_name())
print(pos_2.get_total_income())
