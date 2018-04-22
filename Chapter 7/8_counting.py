# -*- coding: utf-8 -*-

current_number = 0

# вывод на печать только нечетных чисел
while current_number < 10:
    current_number += 1
    # если остаток от деления равен 0, игнорируется остальная программа
    # и происходит возврат к началу
    if current_number % 2 == 0:
        continue
    print(current_number)  # если число не делится без остатка на 2, печатаем
