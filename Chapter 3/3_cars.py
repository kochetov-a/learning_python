# -*- coding: utf-8 -*-

cars = ["bmw", "audi", "toyota", "subaru"]

# constant sorting in alphabetical order
cars.sort()
print(cars)

# constant sorting in reverse alphabetical order
cars.sort(reverse=True)
print(cars)

cars2 = ["bmw", "audi", "toyota", "subaru"]

# temporary sorting by alphabet
print("\nHere is original list: " + str(cars2))
print("\nHere is sorted list: " + str(sorted(cars2)))
print("\nHere is original list again: " + str(cars2))

# sorting by reverse order
cars2.reverse()
print(cars2)

print("Длина списка " + str(len(cars2)))