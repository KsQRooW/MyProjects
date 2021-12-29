doc = open('Coursera_Python/7%_Barier.txt')
x = dict()
for i in doc:
    a = i.split()
    for j in a:
        x[j] = x.get(j, 0) + 1
for j in sorted(x.items(), key=lambda z: (-z[1], z[0])):
    print(j[0])
    break
