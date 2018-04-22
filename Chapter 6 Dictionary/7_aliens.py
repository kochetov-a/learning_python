# -*- coding: utf-8 -*-

aliens = []
for alien_number in range(30):  # создание новых кораблей 30 шт.
    new_alien = {"color": "green", "point": "5", "speed": "slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total: " + str(len(aliens)))

for alien in aliens[:3]:  # изменение свойств первым трём кораблям
    if alien["color"] == "green":
        alien["color"] = "yellow",
        alien["speed"] = "medium",
        alien["points"] = 10

for alien in aliens[0:5]:
    print(alien)
    print("...")
