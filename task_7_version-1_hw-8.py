# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

# вариант 1 формирование комплексного числа на основании его действительных аргументов без мнимого
class ComplexNumber:
    def __init__(self, complex_real_num_1, complex_real_num_2):
        self.complex_num = complex(complex_real_num_1, complex_real_num_2)

    def __add__(self, other):  # не удалось написать работающий код проверки
        new_complex_num1 = self.complex_num + other.complex_num
        return f'Sum of two complex numbers: {new_complex_num1}'

    def __mul__(self, other):
        new_complex_num2 = self.complex_num * other.complex_num
        return f'Product of two complex numbers: {new_complex_num2}'

print('version #1 example')
complex_num_1 = ComplexNumber(-1, 2)
complex_num_2 = ComplexNumber(2, -4)
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)
print()


# вариант 2 формирование комплексного числа на основании из строки вида (a + bj)
class ComplexNumber2:
    def __init__(self, complex_num):
        self.complex_num = complex_num

    def __add__(self, other):
        try:
            new_complex_num1 = complex(self.complex_num) + complex(other.complex_num)
        except ValueError as err:
            return f'{err}! The format must be "a+bj", no space between elements inside string!'
        else:
            return f'Sum of two complex numbers: {new_complex_num1}'

    def __mul__(self, other):
        try:
            new_complex_num2 = complex(self.complex_num) * complex(other.complex_num)
        except ValueError as err:
            return f'{err}! The format must be "a+bj", no space between elements inside string!'
        else:
            return f'Product of two complex numbers: {new_complex_num2}'

print('version #2 example-1')
complex_num_1 = ComplexNumber2('14- 8j')  # некорректно, с пробелом между елементами
complex_num_2 = ComplexNumber2('-18+2j')
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2)
print('version #2 example-2')
complex_num_3 = ComplexNumber2('-1+2j')  # корректный формат аргумента
complex_num_4 = ComplexNumber2('2-4j')
print(complex_num_3 + complex_num_4)
print(complex_num_3 * complex_num_4)
