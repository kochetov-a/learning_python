# -*- coding: utf-8 -*-

current_users = ['Alexey', 'Marina', 'Oleg', 'Sergey', 'Stiven']
new_users = ['ivan', 'andy', 'marina', 'oleg', 'john']

for user in new_users:
    if user.title() in current_users:
        print("Очень жаль " + user.title() + ' но это имя уже используется...')
    else:
        print("Имя " + user + ' свободно, его можно использовать!')