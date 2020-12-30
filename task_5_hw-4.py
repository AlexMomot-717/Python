# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

num_list = [int(i) for i in range(100, 1001) if i % 2 == 0]
print(num_list)


def multiply_num(a, b):
    return a * b


print(reduce(multiply_num, num_list))
