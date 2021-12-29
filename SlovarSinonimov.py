n = int(input())
x = dict()
for i in range(n):
    a = input().split()
    x[a[0]] = a[1]
    x[a[1]] = a[0]
a = input()
print(x.get(a))
