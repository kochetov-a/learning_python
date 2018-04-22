# -*- coding: utf-8 -*-

my_foods = ["pizzas", "falafel", "carrot cake"]
friend_foods = my_foods[:]  # копирование списка

print("\nMy favorite foods are:")
for my_food in my_foods[:]:
    print(my_food)

print("\nMy friends's favorite food are:")
for friend_food in friend_foods[:]:
    print(friend_food)

my_foods.append("cannoli")  # добавление нового элемента в список "my_foods"
friend_foods.append("ice cream")  # добавление нового элемента в список "friend_foods"

print("\nMy favorite foods are:")
for my_food in my_foods[:]:
    print(my_food)

print("\nMy friends's favorite food are:")
for friend_food in friend_foods[:]:
    print(friend_food)

