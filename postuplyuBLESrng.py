a = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
b = open('input1.txt', 'r', encoding='utf8')
x1 = []
z090401 = []
x2 = []
z090403 = []
for i in a:
    x1.append(i.split()[2:])
for i in x1:
    if len(i[-1]) <= 3:
        z090401.append(i)

for i in b:
    x2.append(i.split()[2:])
for i in x2:
    if len(i[-1]) <= 3:
        z090403.append(i)

z090401.sort(key=lambda t: int(t[-1]), reverse=True)
z090403.sort(key=lambda t: int(t[-1]), reverse=True)

res = []
for i in z090401:
    for j in z090403:
        if i[0:-1] == j[0:-1]:
            i.append(j[-1])
            res.append(i)
k = 1
for i in res:
    #if int(i[-2]) <= int(i[-1]):
    print(k, *i)
    k += 1
