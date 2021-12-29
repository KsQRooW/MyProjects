"""
Определите количество школьников, ставших победителями в каждом классе.
Победителями объявляются все, кто набрал наибольшее число баллов по данному классу.
Гарантируется, что в каждом классе был хотя бы один участник.

Структура файла:
    *Фамилия* *Имя* *Класс* *Балл*
    Пример:
        Иванов Сергей 9 80

Формат вывода:
    Выведите три числа: количество победителей олимпиады по 9 классу, по 10 классу, по 11 классу.
"""

doc = open('KolvoPobediteleiPoKlassam.txt', 'r', encoding='utf8')
max9 = max10 = max11 = 0
k9 = k10 = k11 = 0
for line in doc:
    a = line.split()
    if int(a[2]) == 9:
        if int(a[3]) > max9:
            max9 = int(a[3])
            k9 = 1
        elif int(a[3]) == max9:
            k9 += 1
    if int(a[2]) == 10:
        if int(a[3]) > max10:
            max10 = int(a[3])
            k10 = 1
        elif int(a[3]) == max10:
            k10 += 1
    if int(a[2]) == 11:
        if int(a[3]) > max11:
            max11 = int(a[3])
            k11 = 1
        elif int(a[3]) == max11:
            k11 += 1
print(k9, k10, k11)
