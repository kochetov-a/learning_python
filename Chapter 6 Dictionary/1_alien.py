# -*- coding: utf-8 -*-

# словари состоят из ключа и значения
alien_0 = {'color': 'green', 'points': 5}

# добавление новых ключей и значений в словарь
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)
print("The alien is " + alien_0['color'] + ".")

# изменение значения ключа
alien_0['color'] = 'yellow'
print("But now, the alien is " + alien_0['color'] + ".")

del alien_0['x_position']
print(alien_0)

