"""
Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
Слова должны быть отсортированы по убыванию их количества появления в тексте,
а при одинаковой частоте появления — в лексикографическом порядке.
"""

doc = open('ChastotniiAnalis.txt')
x = {}
for i in doc:
    a = i.split()
    for j in a:
        x[j] = x.get(j, 0) + 1
for j in sorted(x.items(), key=lambda z: (-z[1], z[0])):
    print(j[0])
