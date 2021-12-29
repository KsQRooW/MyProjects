doc = open('Coursera_Python/7%_Barier.txt', 'r', encoding='utf8')
a = doc.readline()
k = 0
parties = []
votes = []
flag = False
for line in doc:
    a = line.rstrip()
    if a == 'VOTES:':
        flag = True
        votes = [0] * len(parties)
        continue
    if not flag:
        parties.append(a)
    else:
        k += 1
        votes[parties.index(a)] += 1
for i in range(len(parties)):
    parties[i] = (parties[i], votes[i])
parties.sort(key=lambda x: (-x[1], x[0]))
for i in parties:
    print(i[0])
