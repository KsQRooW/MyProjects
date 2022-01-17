"""
В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой.
У родоначальника высота равна 0, у любого другого элемента высота на 1 больше, чем у его родителя.
Вам дано генеалогическое древо, определите высоту всех его элементов.

Формат ввода:
    Программа получает на вход число элементов в генеалогическом древе N.
    Далее следует N-1 строка, задающие родителя для каждого элемента древа, кроме родоначальника.
    Каждая строка имеет вид имя_потомка имя_родителя.

Формат вывода:
    Программа должна вывести список всех элементов древа в лексикографическом порядке.
    После вывода имени каждого элемента необходимо вывести его высоту.
"""


def rec(a, k):
    for i in a:
        if a.get(i, 0):
            rec(a.get(i), k + 1)
        if treeind.get(i, 0) < k:
            treeind[i] = k
    return


n = int(input())
tree = dict()
for i in range(n - 1):
    x = input().split()
    if x[1] not in tree:
        tree.setdefault(x[1], dict())
        tree[x[1]].setdefault(x[0], dict())
    else:
        tree[x[1]].setdefault(x[0], dict())
for key in tree:
    for chel in tree[key]:
        if chel in tree:
            tree[key][chel] = tree[chel]
treeind = dict()
k = 1
for key in tree:
    rec(tree[key], k)
    if key not in treeind:
        treeind[key] = 0
for key in sorted(treeind):
    print(key, treeind[key])
