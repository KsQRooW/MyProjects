n = int(input())
x = []
for i in range(n):
    x.append(tuple(input().split()))
x.sort(key=lambda a: -int(a[1]))
for element in x:
    print(element[0])
