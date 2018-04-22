# -*- coding: utf-8 -*-

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers)

for n in numbers:
    if n == 1:
        print('\n' + str(n) + 'st')
    elif n == 2:
        print('\n' + str(n) + 'nd')
    elif n == 3:
        print('\n' + str(n) + 'rd')
    else:
        print('\n' + str(n) + 'th')