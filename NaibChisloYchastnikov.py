"""
переделать через dict()
"""

doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
myList = [0] * 99
for i in doc:
    a = i.split()
    myList[int(a[2]) - 1] += 1
maxim = max(myList)
k = myList.count(maxim)
Out = []
z = 0
for i in range(k):
    Out.append(myList.index(maxim, z) + 1)
    z = myList.index(maxim, z) + 1
Out.sort()
print(*Out)
