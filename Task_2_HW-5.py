# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

line_count = 0
with open('file_1_4.txt', encoding='utf-8') as f_object:
    f_object.seek(0)
    for line in f_object:
        line_count += 1
        words_count = line.count(' ') + 1
        print(f"line {line_count} contains {words_count} word(s)")
    print()
    print(f"{f_object.name} contains {line_count} line(s)")



