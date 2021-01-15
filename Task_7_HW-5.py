# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json

d_1 = {}
total_profit = 0
count = 0
with open('text_7.txt', encoding='utf-8') as f:
    for line in f:
        count += 1
        c, t, i, e = line.split(' ')
        result = int(i) - int(e)
        if result > 0:
            total_profit += result
        d_1.update({c: result})
        d_2 = dict({"average profit": int(total_profit / count)})
        companies_fin_list = list([d_1, d_2])
with open('text_777.json', 'w', encoding='utf-8') as f:
    json.dump(companies_fin_list, f, ensure_ascii = False)


