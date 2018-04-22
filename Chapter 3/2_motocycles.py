# -*- coding: utf-8 -*-

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# изменение значения определенного элемента из списка
motorcycles[0] = "bugatti"
print(motorcycles)

# присоеденение элемента в конец списка
motorcycles.append("ducati")
print(motorcycles)

# вставка элемента в список
motorcycles.insert(2, "yupiter")
print(motorcycles)

# удаление элемента из списка по позиции элемента
del motorcycles[1]
print(motorcycles)

# удаление последнего элемента из списка с последующим его использованием
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# удаление произвольного элемента из списка с последующим его использованием
popped_motorcycle = motorcycles.pop(0)
print(motorcycles)
print(popped_motorcycle)

# удаление элемента списка по значению
motorcycles.remove("suzuki")
print(motorcycles)