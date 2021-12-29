doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
x = dict()
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
