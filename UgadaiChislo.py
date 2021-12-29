n = int(input())
x = set(range(1, n + 1))
z = set()
for i in range(n):
    a = input().split()
    if a[0] == 'HELP':
        break
    else:
        b = input()
        if b == 'NO':
            for j in range(len(a)):
                x.discard(int(a[j]))
        elif b == 'YES':
            for j in range(len(a)):
                z.add(int(a[j]))
            x = x - (x - z)
            z = set()
print(*sorted(x))
