doc = open('Coursera_Python/7%_Barier.txt')
x = dict()
for i in doc:
    a = i.split()
    x[a[0]] = x.get(a[0], 0) + int(a[1])
for j in sorted(x.items()):
    print(j[0], j[1])
