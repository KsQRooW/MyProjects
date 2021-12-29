n = int(input())
strani = dict()
for i in range(n):
    a = input().split()
    for j in range(1, len(a)):
        strani[a[j]] = a[0]
m = int(input())
for i in range(m):
    a = input()
    print(strani.get(a))
