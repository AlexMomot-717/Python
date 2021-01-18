# Создать класс TrafficLight (светофор), определить у него один атрибут color (цвет)
# и метод running (запуск); атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться
# только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight:
    __color = ['red', 'yellow', 'green']  # атрибут Класса (приватный)

    # green_time = int(input('Enter duration for green light, sec.: '))
    # loops_number = int(input('Enter a number of traffic light iteration: '))

    def running(self):

        def get_warning_sign():  # предупреждающая о неверном порядке цветов надпись
            print("\033[0m\033[0m")
            print("\033[31mtraffic_light is broken! follow traffic regulations!")
            print("\033[0m\033[0m")

        loops_count = 0
        while loops_count < 1:  # можно количество итераций вводить, можно  вообще убрать цикл while,
            #  тогда прогон светофора только 1 раз будет.
            loops_count += 1
            if TrafficLight.__color[0] == 'red':
                print("\033[31m\033[41m {}".format(TrafficLight.__color[0]))
                time.sleep(2)
            else:
                return get_warning_sign()  # проверка порядка цветов
                # break
            if TrafficLight.__color[1] == 'yellow':
                print("\033[33m\033[43m {}".format(TrafficLight.__color[1]))
                time.sleep(7)
            else:
                return get_warning_sign()  # проверка порядка цветов
                # break
            if TrafficLight.__color[2] == 'green':
                print("\033[32m\033[42m {}".format(TrafficLight.__color[2]))
                time.sleep(3)
                print("\033[0m\033[0m")
                time.sleep(0)
            else:
                return get_warning_sign()  # проверка порядка цветов
                # break


t_1 = TrafficLight()
t_1.running()
print(t_1._TrafficLight__color, end='\n')

# 2. вариант
print('Version 2\n')


class TrafficLight:
    __color = ('red', 'yellow', 'green')  # кортеж! атрибут Класса (приватный)

    def running(self): # завершение скрипта при неверном порядке происходит без дополнительных команд

        if TrafficLight.__color == ('red', 'yellow', 'green'):
            print("\033[31m\033[41m {}".format(TrafficLight.__color[0]))
            time.sleep(2)
            print("\033[33m\033[43m {}".format(TrafficLight.__color[1]))
            time.sleep(7)
            print("\033[32m\033[42m {}".format(TrafficLight.__color[2]))
            time.sleep(3)
            print("\033[0m\033[0m")
            time.sleep(0)
        else:
            print("\033[0m\033[0m")
            print("\033[31mtraffic_light is broken! follow traffic regulations!")
            print("\033[0m\033[0m")


t_1 = TrafficLight()
t_1.running()
print(t_1._TrafficLight__color, end='\n')
