# -*- coding: utf-8 -*-

sandwich_orders = ["бокадильо", "пастрами", "арепа", "пастрами",
                   "крок-мадам", "бан ми", "донер-кебаб", "пастрами"]
print(sandwich_orders)

# пока в списке есть пастрами, продолжаем цикл
while "пастрами" in sandwich_orders:
    sandwich_orders.remove("пастрами")

print(sandwich_orders)