def oneFlag(x, kol):
    flag = False
    for i in range(kol):
        if x[i] == x[i + 1]:
            flag = True
        else:
            flag = False
            break
    return flag


def zer0Flag(x, kol):
    if x <= kol:
        return True
    return False


def checkpoint(x, kol):
    check = 0
    z = 0
    for i in range(len(x) - 1):
        z += 1
        if z == kol:
            if x[i] != x[i + 1]:
                check = x[i]
            else:
                for j in range(i, -1, -1):
                    if x[i] != x[j]:
                        check = x[j]
                        break
            break
    return check


doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
docOut = open('output.txt', 'w', encoding='utf8')
k = int(doc.readline())
myList = []
for i in doc:
    a = i.split()
    if int(a[-3]) >= 40 and int(a[-2]) >= 40 and int(a[-1]) >= 40:
        myList.append((int(a[-3]) + int(a[-2]) + int(a[-1])))
myList.sort(key=lambda z: -z)
if zer0Flag(len(myList), k) or k == 0:
    print(0, file=docOut)
elif oneFlag(myList, k):
    print(1, file=docOut)
else:
    print(checkpoint(myList, k), file=docOut)
