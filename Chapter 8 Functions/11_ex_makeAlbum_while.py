# -*- coding: utf-8 -*-

def make_album(author, album):
    albums = author + " - " + album
    return albums


while True:
    print("\nВведите данные альбома.")
    print("Для выхода из программы введите 'q'.")

    a_author = input("Исполнителя: ")
    if a_author == 'q':
        print("Завершение программы.")
        break

    a_album = input("Название альбома: ")
    if a_album == 'q':
        print("Завершение программы.")
        break

    full_album = make_album(a_author, a_album)
    print(full_album)
