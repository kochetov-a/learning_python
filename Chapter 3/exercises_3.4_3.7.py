# -*- coding: utf-8 -*-
# 3-4
guest = ["Александр Пушкин", "Никита Михалков", "Арнольд Шварценеггер"]
print("Жду тебя, уважаемый " + guest[0] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[1] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[2] + " сегодня вечером на ужин!")

# 3-5
print("К сожалению " + guest[0] + " прийти не сможет...\n")
del guest[0]

guest.append("Лев Толстой")
print("Вместо него ко мне придет " + guest[-1] + "!\n")

print("Жду тебя, уважаемый " + guest[0] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[1] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[2] + " сегодня вечером на ужин!\n")

# 3-6
print("Мой стол может вместить больше гостей!\n")
guest.insert(0, "Оноре Де Бальзак")
guest.insert(2, "Николай Гоголь")
guest.append("Сергей Есенин")

print("Жду тебя, уважаемый " + guest[0] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[1] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[2] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[3] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[4] + " сегодня вечером на ужин!")
print("Жду тебя, уважаемый " + guest[5] + " сегодня вечером на ужин!\n")
print("Итого ожидается вечером " + str(len(guest)) + " человек!!!\n")

# 3-7

print("К сожалению, принять смогу только двух гостей...\n")

not_come = guest.pop(0)
print("Сожалею уважаемый " + not_come + " но не смогу Вас принять сегодня.")

not_come = guest.pop(0)
print("Сожалею уважаемый " + not_come + " но не смогу Вас принять сегодня.")

not_come = guest.pop(0)
print("Сожалею уважаемый " + not_come + " но не смогу Вас принять сегодня.")

not_come = guest.pop(1)
print("Сожалею уважаемый " + not_come + " но не смогу Вас принять сегодня.\n")

print("А вас, уважаемый " + guest[0] + " я по-прежнему жду на ужин!")
print("А вас, уважаемый " + guest[1] + " я по-прежнему жду на ужин!\n")

del guest[0]
del guest[0]
print("Итоговый список гостей: " + str(guest))





