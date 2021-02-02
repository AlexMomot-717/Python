# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    #def __init__(self, date):
        #self.date = date

    @classmethod
    def rearrange_date(cls, date): # так как в этом классе нет "обычных" методов, использую @classmethod и как конструктор
        day, month, year = [int(i) for i in date.split('-')]
        # day, month, year = date_list
        # day = int(date.split('-')[0])
        # month = int(date.split('-')[1])
        # year = int(date.split('-')[2])
        return cls.check_valid(day, month, year)

    @staticmethod
    def check_valid(day, month, year):
        if month > 12:
            return f'Ошибка! В году всего 12 месяцев!'
        elif day <= 0 or month <= 0 or year <= 0:
            return f'Ошибка! Число, месяц и год не могут иметь нулевое или отрицательное значение!'
        elif month in (1, 3, 5, 7, 8, 10, 12) and day > 31:
            return f'Ошибка! В {month:02} месяце всего 31 день!'
        elif month in (4, 6, 9, 11) and day > 30:
            return f'Ошибка! В {month:02} месяце всего 30 дней!'
        if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
            if month == 2 and day > 29:
                return f'Ошибка! Год {year} - високосный, в {month:02} месяце всего 29 дней!'
        else:
            if month == 2 and day > 28:
                return f'Ошибка! В {month:02} месяце {year} года всего 28 дней!'
        if year < 1000:
            return f'Обратите внимание на формат года! Дата условно корректная:\nчисло: ' \
                   f'{day:02}, месяц: {month:02} , год: {year}'

        return f'Проверка выполнена! Дата корректная:\nчисло: {day:02}, месяц: {month:02} , год: {year}'


my_date = Date()
print(my_date.rearrange_date('20-02-2000'), '\n')
print(Date.check_valid(31, 11, 1918), '\n') # если вызывать @staticmethod check_valid самостоятельно,
# то тип и количество аргументов должен быть уже таким. P.S. пыталась через obj, чтобы в формате строки аргумент подавать - не получилось
print(my_date.check_valid(8, 13, 2018), '\n')
print(my_date.rearrange_date('20-00-00'), '\n')
print(my_date.rearrange_date('30-02-1980'), '\n')
print(my_date.rearrange_date('29-02-2002'), '\n')
print(my_date.rearrange_date('05-07-77'), '\n')