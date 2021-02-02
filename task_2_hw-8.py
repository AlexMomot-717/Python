# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class MyZrDvErr(Exception):
    def __init__(self, text):
        self.text = text

while True:
    # a, b = [int(i) for i in (input('Введите через пробел делимое, делитель: ').split())]
    try:
        a, b = [int(i) for i in (input('Введите через пробел делимое, делитель: ').split())]
        if a not in (0,1,2,3,4,5,6,7,8,9) or b not in (0,1,2,3,4,5,6,7,8,9):
            raise ValueError()
        elif b == 0:
            raise MyZrDvErr('Ошибка!Делитель не должен иметь нулевое значение!')

    except MyZrDvErr as err:
        print(err)
        continue
    except ValueError as err:
        print(err, 'Ошибка!Вводите только числа!')
        continue
    else:
        print(f'Результат от деления: {a / b}')
        break


