"""
Дана база данных о продажах некоторого интернет-магазина.
Создайте список всех покупателей,
а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.

Структура файла:
    Каждая строка входного файла представляет собой запись вида
        Покупатель Товар Количество, где
            Покупатель — имя покупателя (строка без пробелов),
            Товар — название товара (строка без пробелов),
            Количество — количество приобретенных единиц товара.
"""

doc = open('Prodaji.txt', 'r', encoding='utf8')
x = {}
for line in doc:
    a = line.split()
    if a[0] not in x:
        x[a[0]] = dict()
    if a[1] not in x[a[0]]:
        x[a[0]].setdefault(a[1], int(a[2]))
    else:
        x[a[0]][a[1]] += int(a[2])
for key in sorted(x):
    print(key + ':')
    for tovar in sorted(x[key]):
        print(tovar, x[key][tovar])