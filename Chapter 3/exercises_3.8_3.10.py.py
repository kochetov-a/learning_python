# -*- coding: utf-8 -*-

# 3-8
country = ["Italy", "Egypt", "USA", "India", "Espanol"]
print("Список стран в которых я бы хотел побывать: " + str(country))
print("Список стран в алфавитном порядке: " + str(sorted(country)))
print("Список стран в обычном порядке: " + str(country))
print("Список стран в обратном алфавитном порядке: " + str(sorted(country, reverse=True)))
print("Список стран в обычном порядке: " + str(country))
country.reverse()
print("Список стран в обратном порядке: " + str(country))
country.reverse()
print("Список стран в исходном порядке: " + str(country))
country.sort()
print("Список стран в алфавитном порядке: " + str(country))
country.sort(reverse=True)
print("Список стран в обратном алфавитном порядке: " + str(country))