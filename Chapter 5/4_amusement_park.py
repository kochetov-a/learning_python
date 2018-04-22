# -*- coding: utf-8 -*-

age = 1

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 25:
    price = 10
else:
    price = 100

print("Your admissions cost is " + str(price) + "$")