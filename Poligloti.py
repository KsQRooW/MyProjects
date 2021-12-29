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

