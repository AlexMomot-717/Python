# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def rearrange_date(cls, date):
        day, month, year = [int(i) for i in date.split('-')]
        return cls(day, month, year)

    @staticmethod
    def check_valid(obj): # если obj заменить на self, также работает
        if obj.month > 12:
            return f'Ошибка! В году всего 12 месяцев!'
        elif obj.day <= 0 or obj.month <= 0 or obj.year <= 0:
            return f'Ошибка! Число, месяц и год не могут иметь нулевое или отрицательное значение!'
        elif obj.month in (1, 3, 5, 7, 8, 10, 12) and obj.day > 31:
            return f'Ошибка! В {obj.month:02} месяце всего 31 день!'
        elif obj.month in (4, 6, 9, 11) and obj.day > 30:
            return f'Ошибка! В {obj.month:02} месяце всего 30 дней!'
        if ((obj.year % 4 == 0) and (obj.year % 100 != 0)) or (obj.year % 400 == 0):
            if obj.month == 2 and obj.day > 29:
                return f'Ошибка! Год {obj.year} - високосный, в {obj.month:02} месяце всего 29 дней!'
        else:
            if obj.month == 2 and obj.day > 28:
                return f'Ошибка! В {obj.month:02} месяце {obj.year} года всего 28 дней!'
        if obj.year < 1000:
            return f'Обратите внимание на формат года! Дата условно корректная:\nдата: ' \
                   f'{obj.day:02}, месяц: {obj.month:02} , год: {obj.year}'

        return f'Проверка выполнена! Дата корректная:\nдата: {obj.day:02}, месяц: {obj.month:02} , год: {obj.year}'


# my_date = Date()
d_1 = Date.rearrange_date('20-02-2000')
print(d_1.day, d_1.month, d_1.year, '\n')
print(d_1.check_valid(d_1), '\n')
d_7 = Date.rearrange_date('31-11-1918')
print(d_7.check_valid(d_7), '\n')
d_2 = Date.rearrange_date('08-13-2018')
print(Date.check_valid(d_2), '\n')
d_3 = Date.rearrange_date('20-00-00')
print(Date.check_valid(d_3), '\n')
d_4 = Date.rearrange_date('30-02-1980')
print(d_4.check_valid(d_4), '\n')
d_5 = Date.rearrange_date('29-02-2002')
print(d_5.check_valid(d_5), '\n')
d_6 = Date.rearrange_date('05-07-77')
print(Date.check_valid(d_6), '\n')

