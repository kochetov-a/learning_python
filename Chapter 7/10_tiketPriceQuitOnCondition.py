# -*- coding: utf-8 -*-

print("Введите ваш возраст: ")

i = 1
while i != 0:
    age = input()
    if age == "quit":
        print("Всего хорошего!")
        i = 0
    elif int(age) <= 3:
        print("Для вас билет бесплатный.")
        continue
    elif 12 >= int(age) > 3:
        print("Для вас билет будет стоить 10$.")
        continue
    elif int(age) >= 12:
        print("Для вас билет будет стоить 15$.")
        continue

