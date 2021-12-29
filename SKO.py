from math import sqrt
n = int(input())
k = 0
sumN = 0
stDev = 0
sko = 1
while n != 0:
    k += 1
    sumN += n
    mean = sumN / k
    stDev += (n - mean) ** 2
    if k != 1:
        sko += sqrt(stDev / (k - 1))
    print(stDev, sko)
    n = int(input())
#stDev = sqrt(stDev / (k - 1))
print(sko)
