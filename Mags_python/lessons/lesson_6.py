import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt

CARS = pd.read_csv('../AUTO21053A.csv', delimiter=';', encoding='utf-8')
col_names = CARS.dtypes.index[CARS.dtypes == 'O'].tolist()

ax = lambda x: plt.subplot(1, 2, x)

# for j, i in enumerate(col_names):
#     ftb = pd.crosstab(CARS[i], i)
#     ftb.index.name = i
#     ftb.columns.name = i
#     ftb.plot.bar(grid=True, colormap='Pastel1', legend=False, ax=ax(j + 1))
#     plt.subplots_adjust(bottom=0.1)

plt.ion()
fig, ax = plt.subplots(1, 1)
while True:
    print("Cols:", col_names)
    col = input("Введите название столбца: ")
    ftb = pd.crosstab(CARS[col], col)
    ftb.index.name = 'Категории'
    ftb.plot.bar(grid=True, colormap='Pastel1', legend=False)
    plt.title(col)

    cnt = input("Продолжить? (да/нет) ")
    if cnt == "да":
        ax.clear()
    else:
        break
    os.system('cls')

plt.ioff()
plt.show()

# https://matplotlib.org/stable/tutorials/colors/colormaps.html?highlight=colormap
