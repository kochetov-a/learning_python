# -*- coding: utf-8 -*-

promtp = "\nНапишите что угодно, и я повторю это:"
promtp += "\nВведите 'quit' для завершения программы."

message = ""
active = True
while active:
    message = input(promtp)
    if message == 'quit':
        active = False
    else:
        print(message)
