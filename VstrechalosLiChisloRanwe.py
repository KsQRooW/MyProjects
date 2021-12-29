a = set()
for i in input().split():
    if i in a:
        print('YES')
    else:
        print('NO')
        a.add(i)
