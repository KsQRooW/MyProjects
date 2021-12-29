"""
переделать через dict()
"""


def CountUpper(a):
    UPCASE = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    k = 0
    for i in range(len(a)):
        if a[i] in UPCASE:
            k += 1
        if k == 2:
            return True
    return False


n = int(input())
slovar = set()
LowSlovar = set()
for i in range(n):
    a = input()
    slovar.add(a)
    LowSlovar.add(a.lower())
x = input().split()
k = 0
for i in range(len(x)):
    if len(x[i]) == 1 and x[i].islower():
        k += 1
    elif x[i].islower() or (x[i].isupper() and len(x[i]) != 1):
        k += 1
    elif x[i].lower() in LowSlovar and x[i] not in slovar:
        k += 1
    elif CountUpper(x[i]):
        k += 1
print(k)
