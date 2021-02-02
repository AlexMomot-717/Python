# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения
# и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


# Вариант без использования метода complex()

class ComplexNumber:
    def __init__(self, compl_num_arg1, compl_num_arg2):
        self.compl_num_arg1 = int(compl_num_arg1)
        self.compl_num_arg2 = int(compl_num_arg2)

    def __str__(self):
        if self.compl_num_arg2 >= 0:
            return f'Complex number: {self.compl_num_arg1}+{self.compl_num_arg2}j'
        else:
            return f'Complex number: {self.compl_num_arg1}{self.compl_num_arg2}j'

    def __add__(self, other):
        if self.compl_num_arg2 + other.compl_num_arg2 >= 0:
            new_complex_num1 = f'Sum of two complex numbers: {self.compl_num_arg1 + other.compl_num_arg1}+{self.compl_num_arg2 + other.compl_num_arg2}j'
        else:
            new_complex_num1 = f'Sum of two complex numbers: {self.compl_num_arg1 + other.compl_num_arg1}{self.compl_num_arg2 + other.compl_num_arg2}j'
        return new_complex_num1

    def __mul__(self, other):
        if (self.compl_num_arg1 * other.compl_num_arg1 + self.compl_num_arg2 * other.compl_num_arg2) >= 0:
            new_complex_num2 = f'Product of two complex numbers: {self.compl_num_arg1 * other.compl_num_arg1 - self.compl_num_arg2 * other.compl_num_arg2}+{self.compl_num_arg1 * other.compl_num_arg1 + self.compl_num_arg2 * other.compl_num_arg2}j'
        else:
            new_complex_num2 = f'Product of two complex numbers: {self.compl_num_arg1 * other.compl_num_arg1 - self.compl_num_arg2 * other.compl_num_arg2}{self.compl_num_arg1 * other.compl_num_arg1 + self.compl_num_arg2 * other.compl_num_arg2}j'
        return new_complex_num2


# examples:
complex_num_1 = ComplexNumber(14, -18)
complex_num_2 = ComplexNumber(-15, 4)
print(complex_num_1 + complex_num_2)
print(complex_num_1 * complex_num_2, '\n')

complex_num_3 = ComplexNumber(1, -2)
complex_num_4 = ComplexNumber(-4, 1)
print(complex_num_3 + complex_num_4)
print(complex_num_3 * complex_num_4, '\n')
print(complex_num_1)
print(complex_num_2)
print(complex_num_3)
print(complex_num_4)
