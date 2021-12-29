"""
Зачет проводится отдельно в каждом классе.
Победителями олимпиады становятся школьники,
которые набрали наибольший балл среди всех участников в данном классе.

Для каждого класса определите максимальный балл,
который набрал школьник, НЕ ставший победителем в данном классе.

Структура файла:
    *Фамилия* *Имя* *Класс* *Балл*
    Пример:
        Иванов Сергей 9 80

Формат вывода:
    Три числа - максимальные баллы по 9, 10, 11 классу у НЕпобедителя
"""

doc = open('MaxBalNePobeditelya.txt', 'r', encoding='utf8')
max9 = []
max10 = []
max11 = []
predmax9 = predmax10 = predmax11 = 0
for line in doc:
    a = line.split()
    if int(a[2]) == 9:
        max9.append(int(a[3]))
    if int(a[2]) == 10:
        max10.append(int(a[3]))
    if int(a[2]) == 11:
        max11.append(int(a[3]))
m9 = max(max9)
m10 = max(max10)
m11 = max(max11)
for element in max9:
    if predmax9 < element < m9:
        predmax9 = element
for element in max10:
    if predmax10 < element < m10:
        predmax10 = element
for element in max11:
    if predmax11 < element < m11:
        predmax11 = element
print(predmax9, predmax10, predmax11)
