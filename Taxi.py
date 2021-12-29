rast = list(map(int, input().split()))
cost = list(map(int, input().split()))
rast.sort(key=lambda x: -x)
cost.sort()
summa = 0
for i in range(len(rast)):
    summa += rast[i] * cost[i]
print(summa)
