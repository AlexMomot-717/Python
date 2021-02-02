# Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента
# и вносить его в список, только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class CheckDigitErr(Exception):
    # def __init__(self, text):
    # self.text = text

    @staticmethod      # работает также, если реализовать через @classmethod или через обычный метод класса
    def get_number_only_list(list_number):
        #list_number = []
        while True:
            s = input('Enter an integer or a real number, positive or negative (for stop enter "end"): ')
            if s == 'end':
                return list_number
            try:
                n = float(s) if '.' in s else int(s)
                if (s[0] != '-' and '.' not in s[1:] and s.isdecimal() == False) or \
                        (s[0] == '-' and '.' not in s[1:] and s[1:].isdecimal() == False) or \
                        ('.' in s[1:] and s[0] != '-' and s[1:].replace('.', "").isdecimal() == False) or \
                        (s[0] == '-' and '.' in s[2:] and s[2:].replace('.', "").isdecimal() == False) or \
                        (s[0] == '-' and s[1] == '.'):
                    raise ValueError()

            except ValueError as err:
                print(err, 'Enter only a number!')
                continue
            else:
                list_number.append(n)
                continue


new_list = []
check_list = CheckDigitErr() # через создание экземпляра класса (по сути, это не имеет смысла для этого класса)
print(check_list.get_number_only_list(new_list))
print(*new_list)
next_list = []
print(CheckDigitErr.get_number_only_list(next_list)) # через вызов метода класса без создания экземпляра
print(*next_list)
