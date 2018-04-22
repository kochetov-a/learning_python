# -*- coding: utf-8 -*-


def get_formatted_name(first_name, last_name, middle_name=""):
    """Возвращает аккуратно отформтированное имя"""
    if middle_name:  # если middle_name присутствует, то возвращаем и его
        full_name = first_name + " " + middle_name + " " + last_name
    else:  # если отсутствует (пустая строка) то возвращаем без него
        full_name = first_name + " " + last_name
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)

musician = get_formatted_name("john", "hooker", "lee")
print(musician)

