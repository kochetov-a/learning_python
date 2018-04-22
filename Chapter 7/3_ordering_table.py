# -*- coding: utf-8 -*-

count_table = input("Сколько столов вы хотите заказать?\n")
count_table = int(count_table)

if count_table > 8:
    print("Для заказа " + str(count_table) + " столов, Вам придется подождать.")
else:
    print(str(count_table) + " столов ждут вас!")
