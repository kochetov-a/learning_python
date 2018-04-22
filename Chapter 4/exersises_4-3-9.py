# -*- coding: utf-8 -*-


# 4-3 (все числа от 1 до 20)
for a in range(1,21):
    print(a)


# 4-4 (вывод списка от 1 до 1 000 000)
list_of_million = []
for i in range(1, 1000001):
    list_of_million.append(i)
# print(list_of_million)

# 4-5 (максимальное, минимальное число и сумма всех чисел списка)
print(min(list_of_million))
print(max(list_of_million))
print(sum(list_of_million))

# 4-6 (нечетные числа от 1 до 20)
for n in range(1, 21, 2):
    print(n)

# 4-7 (числа кратные "3")
for three in range(3,31,3):
    print(three)

# 4-8 (кубы чисел от 1 до 10)
cubs = []
for c in range(1,11):
    cubs.append(c**3)
print(cubs)

# 4-9 (генератор списка кубов)
cubs_gen = [c**3 for c in range(1, 11)]
print(cubs_gen)

cubs_gen = [c**3 for c in range(1,11)]
print(cubs_gen)