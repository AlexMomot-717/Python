income = int(input('Введите значение выручки за текущий период, тыс.руб.: '))
costs = int(input('Введите значение издержек за текущий период, тыс.руб.: '))
result = income - costs
if result > 0:
    print('Вы отработали с прибылью, тыс. руб:', result)
    print('Рентабельность выручки, %:', round(result / income * 100, 1))
    staff_number = int(input('Введите численность сотрудников фирмы, чел.: '))
    if result / staff_number > 1:
        print('Прибыль фирмы в расчете на одного сотрудника, тыс.руб/чел:', round(result / staff_number, 2))
    else:
        print('Прибыль фирмы в расчете на одного сотрудника, руб/чел:', round(result / staff_number * 1000, 2))
elif result == 0:
    print('Вы отработали с "нулевым" результатом.')
else:
    print('Вы отработали с убытком, тыс. руб:', - result)


