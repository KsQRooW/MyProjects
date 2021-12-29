doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
docOut = open('output.txt', 'w', encoding='utf8')
x = dict()
k = 0
for i in doc:
    x[i.strip()] = x.get(i.strip(), 0) + 1
    k += 1
t = 0
for j in sorted(x.items(), key=lambda z: -z[1]):
    if (int(j[1]) / k) > 0.5:
        print(j[0], file=docOut)
        break
    else:
        if t != 2:
            print(j[0], file=docOut)
            t += 1
