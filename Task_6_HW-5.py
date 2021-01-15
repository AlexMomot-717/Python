# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

subj_dict = {}
with open('text_6.txt', 'r', encoding='utf-8') as f:
    f.seek(0)
    for line in f:
        subj, lect, pract, lab = line.split()
        if lect != '-':
            l = int(lect[0: lect.index('(')])
        else:
            l = 0
        if pract != '-':
            p = int(pract[0: pract.index('(')])
        else:
            p = 0
        if lab != '-':
            lb = int(lab[0: lab.index('(')])
        else:
            lb = 0
        hours = l + p + lb
        subj_dict.update({subj: hours})
print(subj_dict)








    # subjects_hours = dict((key, value) for key in (line.split(':') for line in s.split('\n') for value in (line.split(':') for line in s.split('\n')))

