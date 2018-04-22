# -*- coding: utf-8 -*-

sandwich_orders = ["бокадильо", "пастрами", "арепа", "пастрами",
                   "крок-мадам", "бан ми", "донер-кебаб", "пастрами"]
finished_orders = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print("Приготовился " + sandwich.title())
    finished_orders.append(sandwich)

print("\nПриготовленные сендвичи: ")
for finished_sandwich in finished_orders:
    print(finished_sandwich.title())
