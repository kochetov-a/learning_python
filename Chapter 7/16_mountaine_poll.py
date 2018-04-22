# -*- coding: utf-8 -*-

# пустой списко ответов
responses = {}

# установка флага продолжения опроса
polling_active = True

while polling_active:
    name = input("Как вас зовут? ")
    response = input("На какую гору вы хотели бы поднятся? ")

    # Ответ сохраняется в словаре в формате Имя : Ответ
    responses[name] = response

    # Проверка продолжения опроса
    repeat = input("Вы хотели бы продолжить опрос? (да/нет)")
    if repeat == "нет":
        polling_active = False

# Вывод результатов опроса
print("\n--- Результаты опроса ---")
for name, response in responses.items():
    print(name + " хотел бы забраться на гору " + response + ".")

