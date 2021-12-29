a = list(map(int, input().split()))
len_a = len(a)
all_a = [sorted([*enumerate(a)], key=lambda x: x[1])]
for i in range(len_a):
    for j in range(len_a):
        for z in range(len_a):
            if i != j != z and i != z:
                all_a.append(sorted([(i, a[i] - a[j]), (j, a[j]), (z, a[z])], key=lambda x: x[1]))

yes_no_a = ['NO', 'NO', 'NO']
for i in all_a:
    yes_no_a[i[1][0]] = 'YES'
print(yes_no_a)
