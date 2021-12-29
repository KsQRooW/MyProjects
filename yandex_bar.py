n, m = input().split()
n = int(n)
m = int(m)
a = []
for i in range(n):
    z = input()
    a.append(z)
k = int(input())
kokt = []
for i in range(k):
    z = input().split()
    kokt.append(z)
k = len(a) - 2
for j in range(len(kokt)):
    kolvo = int(kokt[j][1])
    while kolvo != 0:
        if a[k].find('\\') != -1 or a[k].find('|') != -1 or a[k].find('/') != -1:
            a[k] = a[k].replace(' ', kokt[j][2])
            k -= 1
            kolvo -= 1
for i in a:
    print(i)
