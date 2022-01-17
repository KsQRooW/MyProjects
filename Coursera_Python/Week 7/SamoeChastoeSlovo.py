"""
Дан текст. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
"""

doc = open('SamoeChastoeSlovo.txt')
x = dict()
for i in doc:
    a = i.split()
    for j in a:
        x[j] = x.get(j, 0) + 1
for j in sorted(x.items(), key=lambda z: (-z[1], z[0])):
    print(j[0])
    break
