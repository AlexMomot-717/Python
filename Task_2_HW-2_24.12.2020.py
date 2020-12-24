# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

n = int(input('Введите количество элементов формируемого списка: '))
list_1 = []
for i in range(n):
    el = input(f'Введите {i + 1}-й элемент списка: ')
    list_1.append(el)
print(f'Первоначальный список: {list_1}')
list_2 = list_1.copy()
for i in range(len(list_1)):  # 1 вариант
    if i % 2 == 0 and i != (len(list_1) - 1):
        el = list_2[i + 1]
        list_1.pop(i + 1)
        list_1.insert(i, el)
print(f'Измененный список: {list_1}')
for i in range(len(list_1)):  # 2 вариант, тогда list_2 не нужен, более короткий код, меньше памяти
    if i % 2 == 0 and i != (len(list_1) - 1):
        list_1[i], list_1[i + 1] = list_1[i + 1], list_1[i]
print(f'Список с обратными изменениями: {list_1}')
new_list = []
for i in range(len(list_1)):  # 3 вариант, нужен еще лист, трудночитаемо (просто попробовать для навыка)
    if i % 2 == 0 and i != (len(list_1) - 1):
        new_list.append(list_1[i + 1])
        new_list.append(list_1[i])
new_list.append(list_1[-1]) if len(list_1) % 2 != 0 else None # сама придумала поставить None, работает!!!
print(f'Измененный список: {new_list}')
