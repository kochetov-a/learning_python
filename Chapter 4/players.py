# -*- coding: utf-8 -*-

players = ["charles", "martina", "michael", "florence", "eli"]
print(players[0:3])  # вывод первый трех элементов списка
print(players[1:4])
print(players[:4])  # от начала списка и до последнего элемента
print(players[2:])  # от второго элемента списка и до конца списка
print(players[-3:])  # вывод трех последних элеметнов списка

print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())


# -*- Exercise 4-10 -*-
elements = ["Element 0", "Element 1", "Element 2", "Element 3", "Element 4", "Element 5"]

print("The first three items in the list are:")
print(elements[0:3])

print("\nThree items from the middle of the list are:")
print(elements[3:])
