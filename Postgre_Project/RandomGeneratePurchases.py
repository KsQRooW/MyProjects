"""
Случайный генератор данных для базы данных
Генерирует следующую строку:
    Номер_заказа, ID_пользователя, ID_товара, Количество, Дата_покупки
"""

import datetime
import random

x = []
orderNumber = range(300)
for i in orderNumber:
    userId = random.randrange(1, 26, 1)
    for j in range(random.randrange(1, 6, 1)):
        itemId = random.randrange(1, 11, 1)
        amount = random.randrange(1, 10, 1)

        x.append((i, userId, itemId, amount))

random_dates = []
for i in range(300):
    start_date = datetime.date(2019, 1, 1)
    end_date = datetime.date(2021, 12, 31)
    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    random_dates.append(random_date)

random_dates.sort()
z = list(map(str, random_dates))

count_orderNumber = 0
for i in range(len(x)):
    if x[i][0] != count_orderNumber:
        count_orderNumber += 1
    x[i] += (z[count_orderNumber],)

for i in x:
    print('  ', i, ',', sep='')
