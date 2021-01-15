# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

with open('text_4.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    d_1 = dict((key, int(value)) for key, value in (line.split(' - ') for line in s.split('\n')))
    d_2 = dict((key, value) for key, value in zip(['Один', 'Два', 'Три', 'Четыре'], d_1.values()))
with open('text_4_1.txt', 'w', encoding='utf-8') as f_1:
    for key, value in d_2.items():
        print(f'{key} - {value}', file=f_1)




