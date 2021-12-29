from math import ceil
doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
docOut = open('output.txt', 'w', encoding='utf8')
x = dict()
k = 0
for i in doc:
    a = i.split()
    name = ''
    for j in range(len(a) - 1):
        name += a[j] + ' '
    name = name[:-1]
    x[name] = x.get(name, 0) + int(a[-1])
    k += int(a[-1])
FirstIzbChastnoe = k / 450
z = []
a = 450
for key in x:
    v = x.get(key) / FirstIzbChastnoe
    z.append([key, v])
    a -= int(x.get(key) / FirstIzbChastnoe)
z.sort(key=lambda p: -(p[1] - int(p[1])))
for i in range(a):
    if z[i][1] - int(z[i][1]) == z[i + 1][1] - int(z[i + 1][1]) and i != a - 1:
        if x[z[i][0]] > x[z[i + 1][0]]:
            z[i][1] = ceil(z[i][1])
        else:
            z[i + 1][1] = ceil(z[i + 1][1])
    z[i][1] = ceil(z[i][1])
for i in range(a, len(z)):
    z[i][1] = int(z[i][1])
for i in range(len(z)):
    x[z[i][0]] = z[i][1]
for key in x:
    print(key, x[key])
