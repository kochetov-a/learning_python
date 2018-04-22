# -*- coding: utf-8 -*-

promtp = "\nВведите название городов, которые вы посещали."
promtp += "\n(введите 'quit' для выхода из программы)"

while True:
    city = input(promtp)
    if city == 'quit':
        break
    else:
        print("Я бы тоже хотел посетить " + city.title() + "!")
