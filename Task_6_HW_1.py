a = int(input('Введите первоначальный результат спортсмена, км: '))
b = int(input('Введите необходимый итоговый результат спортсмена, км: '))
result = a
days = 1
print(str(days) + '-й день:', result)
while result <= b:
    result = round(result * 1.1, 2)
    days += 1
    print(str(days) + '-й день:', result)
print('на', str(days) + '-й день спортсмен достиг результата — не менее ', b, 'км')
