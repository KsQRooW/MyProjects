doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
sr9 = sr10 = sr11 = 0
k9 = k10 = k11 = 0
for line in doc:
    a = list(line.split())
    if a[2] == '9':
        sr9 += int(a[3])
        k9 += 1
    if a[2] == '10':
        sr10 += int(a[3])
        k10 += 1
    if a[2] == '11':
        sr11 += int(a[3])
        k11 += 1
print(sr9 / k9, sr10 / k10, sr11 / k11)
doc.close()
