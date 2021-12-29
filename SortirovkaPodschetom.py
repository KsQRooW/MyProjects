def CountSort(a):
    for element in a:
        z[element] += 1


x = list(map(int, input().split()))
z = [0] * 101
CountSort(x)
for i in range(len(z)):
    for j in range(z[i]):
        print(i, end=' ')

