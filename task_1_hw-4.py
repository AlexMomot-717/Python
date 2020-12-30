# Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

name, work_hours, hour_rate, bonus = argv

print(argv)


def wages_calc(name, work_hours, hour_rate, bonus):
    return print(f"Employee's wages for hours worked: {((int(work_hours) * int(hour_rate)) + int(bonus))}")


wages_calc(name, work_hours, hour_rate, bonus)

