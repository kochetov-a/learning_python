# -*- coding: utf-8 -*-

# проверка специальных значений
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Просим прощения, у нас нет зеленого перца сейчас.')
    else:
        print('\nДобавляем ' + requested_topping + '.')
print('\nПриготовление пиццы закончено!')

# проверка наличия элементов в списке
requested_toppings2 = []

if requested_toppings2:
    for requested_topping2 in requested_toppings2:
        print('Добавляем ' + requested_toppings2 + '.')
        print('Завершено приготовление пиццы.')
else:
    print('\nВы действительно хотите стандартную пиццу?')

# множественные списки
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni',
                      'pineapple', 'extra cheese']
requested_toppings3 = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping3 in requested_toppings3:
    if requested_topping3 in available_toppings:
        print('Добавляем ' + requested_topping3 + '.')
    else:
        print('\nИзвините, у нас нет ' + requested_topping3 + '.')
print('Приготовление пиццы завершено.')