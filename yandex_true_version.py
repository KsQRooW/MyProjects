version = list(map(int, input().split()))
n = int(input())

rules = []
for i in range(n):
    z = list(map(int, input().split()))
    rules.append(z)


for i in range(len(rules)):
    for j in range(i + 1, len(rules)):
        if len(rules[i]) == 4 == len(rules[j]):
            if rules[i][0] == rules[j][2] and rules[i][2] == rules[j][0]:
                if rules[i][3] > rules[j][1] and rules[i][1] < rules[j][3]:
                    rules.append([rules[i][0], rules[i][1]])
                    if j + 2 >= len(rules):
                        break

counter = 0
for i in rules:
    if len(i) == 2:
        index = [1, 2, 3]
        index.remove(i[0])
        q = (version[i[0] - 1] ** 0) * version[index[0] - 1] * version[index[1] - 1]
        counter -= q
    else:
        index = [1, 2, 3]
        index.remove(i[0])
        index.remove(i[2])
        q = (version[i[0] - 1] - i[1] + 1) * (i[3] - 1) * version[index[0] - 1]
        counter += q

print(version[0] * version[1] * version[2] - counter)
