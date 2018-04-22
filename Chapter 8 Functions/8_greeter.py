# -*- coding: utf-8 -*-


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name


while True:
    print("\nВведите свое имя: ")
    print("Или введите 'q' для завершения программы.")

    f_name = input("\nИмя: ")
    if f_name == 'q':
        print("До свидания!")
        break

    l_name = input("Фамилия: ")
    if l_name == 'q':
        print("До свидания!")
        break

    formatted_name = get_formatted_name(f_name.title(), l_name.title())
    print(formatted_name)
    

