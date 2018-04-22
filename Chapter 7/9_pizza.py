# -*- coding: utf-8 -*-

print("Введите название дополнения для пиццы: ")

while True:
    pName = input()
    if pName == "quit":
        print("Всего хорошего!")
        break
    print("Дополнение '" + pName + "' включено в заказ!")

