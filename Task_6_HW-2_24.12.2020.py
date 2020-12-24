# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
n = int(input('Введите количество товарных позиций: '))
goods_list = []
goods_name = []
goods_price = []
goods_quantity = []
goods_unit = []
for i in range(n):
    # вводить значения ключей сразу в теле функции dict - это мой эксперимент, нигде не искала! работает!!!!!
    good_dict = dict(название=input('введите название товара: '), цена=input('введите цену товара: '),
                     количество=input('введите количество товара: '), ед=input('введите единицу измерения товара: '))
    good_card = tuple((i + 1, good_dict))
    goods_list.append(good_card)
    goods_name.append(good_dict.get('название'))
    goods_price.append(good_dict.get('цена'))
    goods_quantity.append(good_dict.get('количество'))
    goods_unit.append(good_dict.get('ед'))
goods_unit = set(goods_unit)
# на примере совпадающие единицы изм. не повторяются, лучше ничего не нашла,
# как сделать две тикие трансформации
goods_unit = list(goods_unit)
print('Структура данных «Товары»: ', goods_list, sep='\n')
goods_analytics = dict(название=goods_name, цена=goods_price, количество=goods_quantity, ед=goods_unit)
print('Аналитика о товарах: ', goods_analytics, sep='\n')
