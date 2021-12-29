n = int(input())
x = set(range(1, n + 1))
y = set()
for i in range(n):
    a = input().split()
    if a[0] == 'HELP':
        break
    else:
        z = set(map(int, a))
        if len(z & x) <= len(x) / 2:
            print('NO')
            for j in range(len(a)):
                x.discard(int(a[j]))
        else:
            print('YES')
            for j in range(len(a)):
                y.add(int(a[j]))
            x = x - (x - y)
            y = set()
print(*sorted(x))
