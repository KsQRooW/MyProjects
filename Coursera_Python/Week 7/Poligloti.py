"""
Каждый из N школьников некоторой школы знает Mᵢ языков.
Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.

Формат ввода:
    Первая строка входных данных содержит количество школьников N.
    Далее идет N чисел Mᵢ, после каждого из чисел идет Mᵢ строк, содержащих названия языков,
    которые знает i-й школьник.
    Длина названий языков не превышает 1000 символов,
    количество различных языков не более 1000.
    1≤N≤1000, 1≤Mᵢ≤500.

Формат вывода:
    В первой строке выведите количество языков, которые знают все школьники.
    Начиная со второй строки - список таких языков.
    Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
"""

n = int(input())
vseyaziki = set()
odinyazik = []
for i in range(n):
    z = int(input())
    y = set()
    for j in range(z):
        x = input()
        vseyaziki.add(x)
        y.add(x)
    odinyazik.append(y)
p = odinyazik[0]
for i in range(len(odinyazik)):
    p &= odinyazik[i]
print(len(p))
print(*p, sep='\n')
print(len(vseyaziki))
print(*vseyaziki, sep='\n')
