"""
Дан список партий и список голосов избирателей в файле 7%_Barier.txt
Необходимо вывести спиоск партий, которые попадут в Гос. Думу
При условии, что в Гос. Думу попадают партии, которые набрали
Не менее 7% от числа голосов избирателей.
Вывести партии необходимо в том порядке, в котором они следуют
в файле после слова PARTIES:

Структура файла:
    после слова PARTIES: идут названия партий
    после слова VOTES: идут голоса за партию (1 строка - 1 голос за одну партию)
"""

doc = open('7%_Barier.txt', 'r', encoding='utf8')
doc.readline()  # Пропускаем строку PARTIES:

parties = {}
order_of_parties = []
for line in doc:
    if line.rstrip() == 'VOTES:':
        break
    parties.setdefault(line.rstrip(), 0)
    order_of_parties.append(line.rstrip())

number_of_voters = 0
for line in doc:
    parties[line.rstrip()] += 1
    number_of_voters += 1

threshold = 0.07
for party in order_of_parties:
    value = parties[party] / number_of_voters
    if value >= threshold:
        print(party)
