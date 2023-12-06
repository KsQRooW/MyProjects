"""
Для поступления в вуз абитуриент должен предъявить результаты трех экзаменов в виде ЕГЭ,
каждый из них оценивается целым числом от 0 до 100 баллов.
При этом абитуриенты, набравшие менее 40 баллов по любому экзамену из конкурса выбывают.
Остальные абитуриенты участвуют в конкурсе по сумме баллов за три экзамена.

В конкурсе участвует N человек, при этом количество мест равно K.
Определите проходной балл, то есть такое количество баллов, что количество участников,
набравших столько или больше баллов не превосходит K, а при добавлении к ним абитуриентов,
набравших наибольшее количество баллов среди непринятых абитуриентов,
общее число принятых абитуриентов станет больше K.

Формат ввода:
    Программа получает на вход количество мест K.
    Далее идут строки с информацией об абитуриентах,
    каждая из которых состоит из имени (текстовая строка содержащая произвольное число пробелов)
    и трех чисел от 0 до 100, разделенных пробелами.

    Используйте для ввода файл input.txt с указанием кодировки utf8.

Формат вывода:
    Программа должна вывести проходной балл в конкурсе.
    Выведенное значение должно быть минимальным баллом, который набрал абитуриент, прошедший по конкурсу.
    Также возможны две ситуации, когда проходной балл не определен.
    Если будут зачислены все абитуриенты, не имеющие неудовлетворительных оценок, программа должна вывести число 0.
    Если количество имеющих равный максимальный балл абитуриентов больше чем K, программа должна вывести число 1.
    Используйте для вывода файл output.txt с указанием кодировки utf8.
"""


def oneFlag(x, kol):
    flag = False
    for i in range(kol):
        if x[i] == x[i + 1]:
            flag = True
        else:
            flag = False
            break
    return flag


def zer0Flag(x, kol):
    if x <= kol:
        return True
    return False


def checkpoint(x, kol):
    check = 0
    z = 0
    for i in range(len(x) - 1):
        z += 1
        if z == kol:
            if x[i] != x[i + 1]:
                check = x[i]
            else:
                for j in range(i, -1, -1):
                    if x[i] != x[j]:
                        check = x[j]
                        break
            break
    return check


doc = open('ProhodnoiBal.txt', 'r', encoding='utf8')
docOut = open('ProhodnoiBal_Out.txt', 'w', encoding='utf8')
k = int(doc.readline())
myList = []
for i in doc:
    a = i.split()
    if int(a[-3]) >= 40 and int(a[-2]) >= 40 and int(a[-1]) >= 40:
        myList.append((int(a[-3]) + int(a[-2]) + int(a[-1])))
myList.sort(key=lambda z: -z)
if zer0Flag(len(myList), k) or k == 0:
    print(0, file=docOut)
elif oneFlag(myList, k):
    print(1, file=docOut)
else:
    print(checkpoint(myList, k), file=docOut)