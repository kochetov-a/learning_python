# -*- coding: utf-8 -*-

squares = []
for number in range(1,11):
    squares.append(number**2)

print(squares)

numbers = [1,2,3,4,5,6,7,8,9,10]
print(max(numbers))
print(min(numbers))
print(sum(numbers))

squares2 = [value**2 for value in range(1,11)]
print(squares2)