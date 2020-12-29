# Реализовать функцию my_func(), которая принимает три позиционных аргумента
# и возвращает сумму наибольших двух аргументов.

def my_func(n1, n2, n3):
    """Return sum of two maximal arguments.

    Add all arguments, subtract the minimal argument.
    """
    sum_ = sum([n1, n2, n3]) - min(n1, n2, n3)
    return print(f'сумма наибольших двух аргументов: {sum_}')


my_func(49 ** 3, 7891 // 2, 418917 % 3)
my_func(4, 4, 4)
