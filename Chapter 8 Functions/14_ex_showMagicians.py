# -*- coding: utf-8 -*-

great_magicians = []
magicians = ["Джонатан Пендрэгон", "Данте", "Гарри Блэкстоун", "Сирил Такаяма",
             "Гарри Гудини"]


# печатает список фокусников
def show_magicians(magicians):
    for magician in magicians:
        print("Фокусник: " + magician)


# добавляет к имени фокусника слово "Великий"
def make_great(magicians):
    while magicians:  # пока в списке "magicians" есть элементы
        great_magician = "Великий " + magicians.pop()
        great_magicians.append(great_magician)
    while great_magicians:  # пока в списке "great_magicians" есть элементы
        great_magician = great_magicians.pop()  # вырезаем последний элемент
        magicians.append(great_magician)  # вставляем в другой список
    return magicians


make_great(magicians[:])
show_magicians(magicians)

make_great(magicians)
show_magicians(magicians)
