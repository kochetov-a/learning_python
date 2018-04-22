# -*- coding: utf-8 -*-

# -*- Exercise 5-3 -*-
alien_color = 'red'
if alien_color == 'red':
    print('You have 5 point')
if alien_color == 'green':
    print('Nothing matter.')

# -*- Exercise 5-4 -*-
alien_color2 = 'green'
if alien_color2 == 'red':
    print('You have the 5 point!')
else:
    print("You have the 10 point!")

# -*- Exercise 5-5 -*-

colour = 'yellow'
if colour == 'green':
    print("Вы выиграли 5 очков!")
elif colour == 'yellow':
    print('Вы выиграли 10 очков!')
else:
    print('Вы выиграли 15 очков!')

# -*- Exercise 5-6 -*-
age = 65;

if age < 2:
    print('Вы - младенец.')
elif age >= 2 and age < 4:
    print("Вы - малыш.")
elif age >=4 and age < 13:
    print("Вы - ребенок.")
elif age >=13 and age < 20:
    print('Вы - подросток.')
elif age >=20 and age < 65:
    print('Вы - взрослый')
elif age >=65:
    print('Вы - пожилой человек.')

# -*- Exercise 5-6 -*-
fruit = ['яблоки', 'апельсины', 'вишни', 'мандарины', 'бананы']

if 'яблоки' in fruit:
    print('Ты любишь ' + fruit[0])