# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open('text_5.txt', 'w+', encoding='utf-8') as f:
    numbers = input("Enter numbers separated with space: ")
    f.writelines(numbers)
    num_list = [int(n) for n in numbers.split(' ')]
    print(f'Total = {sum(num_list)}')

