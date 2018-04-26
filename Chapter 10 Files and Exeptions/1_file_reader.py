filename = 'pi_digits.txt'  # сохраняем имя файла в переменную

with open('pi_digits.txt') as file_object:  # открываем файл
    contents = file_object.read()  # читаем содержимое и сохраняем в переменной
    print(contents.rstrip() + "\n")  # выводим на печать переменную

with open(filename) as file_object:  # открываем файл
    for line in file_object:  # читаем содержимое и сохраняем в переменной
        print(line.rstrip())  # перебираем с помощью цикла всё содержимое файла

with open(filename) as file_object:  # открываем файл
    lines = file_object.readlines()  # последовательно чтение каждой строчки и сохранение в список
    for line in lines:
        print(line.rstrip())  # перебираем с помощью цикла всё содержимое файла
