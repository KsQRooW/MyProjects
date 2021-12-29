n, k = map(int, input().split())
setBast = set()
suturday = set(range(6, n + 1, 7))
sunday = set(range(7, n + 1, 7))
for i in range(k):
    a, b = map(int, input().split())
    for j in range(a, n + 1, b):
        setBast.add(j)
print(len(setBast - suturday - sunday))
