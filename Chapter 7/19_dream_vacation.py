# -*- coding: utf-8 -*-

responses = {}
poll_active = True

while poll_active:
    name = input("Как вас зовут? ")
    response = input("Где бы вы хотели отдохнуть? ")

    responses[name] = response
    repeat = input("Вы хотите продолжить опрос? (да / нет) ")
    if repeat == "нет":
        poll_active = False

print("\n--- Результаты опроса ---")

for name, response in responses.items():
    print(str(name.title()) + " хочет поехать на/в " + str(response.title())
          + ".")
