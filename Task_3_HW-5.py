#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и
#  величину их окладов. Определить, кто из сотрудников имеет оклад менее 20 тыс.,
#  вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.

with open('text_3.txt', 'r', encoding='utf-8') as f:
    p = f.read()
    total = 0
    print('Сотрудники с окладом менее 20000,0: ')
    payroll = dict((key, float(value)) for key, value in (line.split(' ') for line in p.split('\n')))
    for surname, income in payroll.items():
        total += income
        if income < 20000:
            print(surname)
average_income = total / len(payroll)
print(f'\nСредняя величина дохода сотрудников: {average_income}')
