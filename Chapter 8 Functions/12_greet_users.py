# -*- coding: utf-8 -*-

def greet_users(names):
    for name in names:
        print("Привет, " + name.title() + "!")


user_names = {"алексей", "марина", "сергей"}
greet_users(user_names)


