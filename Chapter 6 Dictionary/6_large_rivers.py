# -*- coding: utf-8 -*-

large_rivers = {
    "Nile": "Egypt",
    "Dnepr": "Ukraine",
    "Amazonka": "NA"
}

# вывод всего списка
for river, country in sorted(large_rivers.items()):
    print("The " + river.title() + " runs though " + country.title())

print("\n")

# вывод названия реки
for river in sorted(large_rivers.keys()):
    print(river.title())

print("\n")

# вывод страны
for country in sorted(large_rivers.values()):
    print(country.title())