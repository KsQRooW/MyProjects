from itertools import product
from math import log2, ceil


n, a, b = map(int, input().split())
commits = input()

steps = ()
# for i in product(('Л', 'Х'), repeat=3):
#     steps += (i, )

center = n // 2 if (n - 1) % 2 == 0 else n // 2 - 1
start = 0
end = n
k = 0

garant_time = []
if commits[center + 1:end].find('B') == -1:
    garant_time.append(a)
else:
    garant_time.append(b)

i = ceil(log2(n))

while i != 0 and start != center and center != end:
    i -= 1
    print('начало:', start)
    print('середина:', center)
    print('конец:', end)
    print('время:', garant_time)
    print(i)
    print()
    k += 1
    if commits[start:center].find('B') != -1:
        if commits[center + 1:end].find('B') != -1:
            steps += (k, )
    if commits[start:(center + start) // 2 if (center + start) % 2 == 0 else (center + start) // 2 + 1].find('B') == -1:
        if commits[center + 1:(center + end - 1) // 2 if (center + end - 1) % 2 == 0 else (center + end - 1) // 2 + 1 + 1].find('B') == -1:
            steps += (k, )
            end = center
            center = (center + start) // 2 if (center + start) % 2 == 0 else (center + start) // 2 + 1
            garant_time.append(a)
        else:
            if ((center + end - 1) // 2 if (center + end - 1) % 2 == 0 else (center + end - 1) // 2 + 1) == center:
                end = center
                center = (center + start) // 2 if (center + start) % 2 == 0 else (center + start) // 2 + 1
            else:
                start = center
                center = (center + end - 1) // 2 if (center + end - 1) % 2 == 0 else (center + end - 1) // 2 + 1
            garant_time.append(b)
    else:
        if ((center + start) // 2 if (center + start) % 2 == 0 else (center + start) // 2 + 1) == center:
            start = center
            center = (center + end - 1) // 2 if (center + end - 1) % 2 == 0 else (center + end - 1) // 2 + 1
        else:
            end = center
            center = (center + start) // 2 if (center + start) % 2 == 0 else (center + start) // 2 + 1
        garant_time.append(b)
print(steps)
print(sum(garant_time[0:len(garant_time) - 1]))
