# -*- coding: utf-8 -*-


def describe_pet(animal_type, pet_name):
    """Выводит информация о животном"""
    print("\nУ меня есть " + animal_type + ".")
    print("Имя моего " + animal_type + "а — " + pet_name.title() + ".")


describe_pet("кот", "Кузя")
describe_pet("хомяк", "Хома")
describe_pet(animal_type="лошадь", pet_name="Лорд")
