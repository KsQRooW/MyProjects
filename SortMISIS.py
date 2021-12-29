a = open('input1.txt', 'r', encoding='utf8')
x = []
z = []
for i in a:
    x.append(i.split()[2:])
for i in x:
    if len(i[-1]) <= 3:
        z.append(i)
k = 1
for i in sorted(z, key=lambda t: int(t[-1]), reverse=True):
    print(k, *i)
    k += 1
