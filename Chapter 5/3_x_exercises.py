# -*- coding: utf-8 -*-

car = "subaru"

print(car == "subaru")
print(car == "audi")

car = "bmw"
print(car == "bmw")
print(car == "BMW")
print(car.upper() == "BMW")

users_1 = ["alexey", "marina", "kuzma"]
user1 = "alexey"
user2 = "oleg"

if user1 in users_1:
    print(user1.title() + " you are in list!")

if user2 not in users_1:
    print("\n" + user2.title() + " you are not in list!")
    print("\n" + user1.title() + " you are in list!")