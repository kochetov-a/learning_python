# -*- coding: utf-8 -*-

# объявление словаря
favorite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

# перебор всех ключей словаря
for name in favorite_language.keys():
    print(name.title())

print("\n")

# перебор всех ключей и вывод особого значения для друзей
friends = ["phil", "sarah"]
for name in favorite_language.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
        favorite_language[name].title() + "!")

print("\n")

# сортированный вывод
for name, language in sorted(favorite_language.items()):
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

print("\n")

# перебор значений в словаре
print("The following languages have been mentioned:")
for language in favorite_language.values():
    print(language.title())

print("----")