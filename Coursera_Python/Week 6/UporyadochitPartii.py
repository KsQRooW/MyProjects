"""
Выведите список всех партий, участвовавших в выборах,
отсортировав его в порядке убывания количества голосов избирателей,
а при равном количестве голосов - в лексикографическом порядке.

Структура файла:
    после слова PARTIES: идут названия партий
    после слова VOTES: идут голоса за партию (1 строка - 1 голос за одну партию)
"""

doc = open('UporyadochitPartii.txt', 'r', encoding='utf8')
a = doc.readline()
parties = {}
flag = False
for line in doc:
    a = line.rstrip()
    if a == 'VOTES:':
        flag = True
        continue
    if not flag:
        parties[a] = 0
    else:
        parties[a] += 1
for i in sorted(parties.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])
