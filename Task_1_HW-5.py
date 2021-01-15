#  Создать программно файл в текстовом формате,
#  записать в него построчно данные, вводимые пользователем.
#  Об окончании ввода данных свидетельствует пустая строка.

with open('file_1_4.txt', 'w+', encoding='utf-8') as f_object:
    some_data = input('Enter some content in line: ')
    while True:
        f_object.writelines(some_data)
        f_object.writelines('\n')
        some_data = input('Enter some content in line: ')
        if some_data == '':
            break
    f_object.seek(0)
    check_data = f_object.readlines()
    print(check_data)
