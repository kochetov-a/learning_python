# -*- coding: utf-8 -*-

users = ['Alexey', 'Marina', 'Oleg', 'Sergey', 'Jony', 'admin']

if users:
    for user in users:
        if user == 'admin':
            print('Привет, ' + user + '! Хочешь посмотреть дневной отчет?')
        else:
            print('Привет, ' + user + '! Рады видеть тебя на сайте.')
else:
    print("Нам нужны пользователи!")
