# Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
string = input('Введите строку из нескольких слов, разделённых пробелами: ')
print(str)
words_list = string.split()
print(words_list)
for i, el in enumerate(words_list):
    print(i + 1, el[:10])
# или так:
for i, el in enumerate(words_list, 1):
    print(i, el[:10])