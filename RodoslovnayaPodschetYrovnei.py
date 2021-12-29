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
