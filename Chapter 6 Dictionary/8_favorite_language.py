# -*- coding: utf-8 -*-

favorite_language = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskel"]
}

for name, languages in favorite_language.items():
    if len(languages) > 1:  # если в списке языков больше одного языка
        print(name.title() + "'s favorite languages are: ")
        for language in languages:
            print("\t" + language.title())
    else:
        print(name.title() + "'s favorite language is: ")
        for language in languages:
            print("\t" + language.title())
