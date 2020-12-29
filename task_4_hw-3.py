# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

#  1 способ возведения числа в отрицательную степень:
def my_func_1(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0:
            print("x must be actual positive number!")
        elif y >= 0:
            print("y must be negative integer number!")
        else:
            return print(x ** y)
    except (TypeError, ValueError) as error:
        print(error)

my_func_1(input('x = '), input('y = '))

# 2 способ возведения числа в отрицательную степень:
def my_func_2(x, y):
    try:
        x = float(x)
        y = int(y)
        if x <= 0:
            print("x must be actual positive number!")
        elif y >= 0:
            print("y must be negative integer number!")
        else:
            exp_ = 1
            for _ in range(1, - y + 1):
                exp_ /= x
            return print(exp_)
    except (TypeError, ValueError) as error:
        print(error)


my_func_2(input('x = '), input('y = '))
