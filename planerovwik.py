import datetime
import pathlib

file = open('planerovwik.txt', encoding='utf8')
myList = []
for i in file.readlines():
    x = i.rstrip().split(', ')
    if len(x[1].split('.')) == 3:
        x[1] = datetime.datetime.strptime(x[1], '%d.%m.%Y').date()
    else:
        x[1] = datetime.datetime.today().replace(year=3000).date()
    myList.append(x)
myList.sort(key=lambda z: z[1])

path = pathlib.Path('C:/Users/diman/Desktop/itog.txt')

with path.open('w') as a:
    for (i, j) in zip(myList, range(1, len(myList) + 1)):
        ost_vremeni = (i[1] - datetime.datetime.today().date()).days

        if ost_vremeni > 100:
            ost_vremeni = 'сколько хочешь времени'
        a.write('\n' + str(j) + ') ' + str(i[0]) + '\n' + '\tОСТАЛОСЬ ВРЕМЕНИ (дней): ' + str(ost_vremeni) + '\n')
        # print(j, ') ', i[0], '\n', '\t___ ОСТАЛОСЬ ВРЕМЕНИ (дней): ', ost_vremeni, sep='')

        if type(ost_vremeni) == int:
            a.write('\t' + 'Нужно успеть до: ' + str(i[1].strftime('%A, %d %B')) + '\n')
            # print('\t', '___ Нужно успеть до: ', i[1].strftime('%A, %d %B'), '\n', sep='')

