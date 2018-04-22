# -*- coding: utf-8 -*-

users = {
    "aenstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

# вывод всех данныхо пользователе
for user_name, user_info in users.items():
    print("\nUsername: " + user_name)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())