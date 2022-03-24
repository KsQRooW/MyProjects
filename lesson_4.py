# -*- coding: utf-8 -*-
import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import seaborn as sns
import numpy.random as rnd  # Генерация случайных чисел

#  1 ****************** Чтение csv файлов ******************
Stuff = np.array([['Номер', 'Фамилия', 'Департамент', 'Зарплата'],
                  [1, 'Петров', 'маркетинг', 34000],
                  [2, 'Федоров', 'финансы', 35000],
                  [3, 'Ткачева', 'финансы', 22000],
                  [4, 'Самсонова', 'маркетинг', 36000],
                  [5, 'Каштанов', 'маркетинг', 26000]], dtype='O')

np.savetxt('Stuff.csv', Stuff, fmt='%s', delimiter=';')

Stuff1 = np.loadtxt('Stuff.csv', delimiter=';',
                    encoding='cp1251', dtype='O')
type(Stuff1[1, 0])  # Все преобразовалось в строки


def prsf(s):
    """
    Парсер float/str

    Parameters
    ----------
    s : объект
    Returns
    -------
    str или float
    """
    try:
        return float(s)
    except ValueError:
        return str(s)


def prsi(s):
    """
    Парсер int/str

    Parameters
    ----------
    s : объект
    Returns
    -------
    str или int
    """
    try:
        return int(s)
    except ValueError:
        return str(s)


cnv1 = {0: prsi, 1: prsf, 2: prsf, 3: prsf}
cnv2 = {0: prsi, 1: str, 2: str, 3: prsf}

S1 = np.loadtxt('Stuff.csv', delimiter=';', converters=cnv1,
                encoding='cp1251', dtype='O')

S2 = np.loadtxt('Stuff.csv', delimiter=';', converters=cnv2,
                encoding='cp1251', dtype='O')

# # 2 ****************** Отбор ******************
# Отбор
SEL_COL = S1[0, :] == 'Департамент'
SEL_ROW = (S1[:, SEL_COL] == 'маркетинг')
# |(S1[:, SEL_COL] == 'Департамент')
SEL_ROW.shape = (SEL_ROW.shape[0],)
S11 = S1[SEL_ROW, :]
S11A = S1[SEL_ROW, [0, 1, 3]]
S12 = S1[np.ix_(SEL_ROW, [0, 1, 3])]
# # 3 ****************** Интерактивный режим ********************
Z = np.empty(shape=(100, 4), dtype=float)
Z[:, 0] = np.linspace(-1, 2, 100)
Z[:, 1] = 2 + 3 * Z[:, 0]
Z[:, 2] = (Z[:, 0] - 1) * (Z[:, 0] + 0.5)
Z[:, 3] = Z[:, 0] * (Z[:, 0] - 1) * (Z[:, 0] + 0.5)
plt.ion()
fig, ax = plt.subplots(1, 1)
while True:
    ans = input("Введите номер функции: ")
    n = int(ans)
    line = ax.plot(Z[:, 0], Z[:, n])
    ans = input("Введите подпись: ")
    ax.set_title(ans)
    ans = input("Введите цвет ('r', 'b', 'g', ...): ")
    plt.setp(line, color=ans)
    cnt = input("Продолжить? (да/нет) ")
    if cnt == "да":
        ax.clear()
    else:
        break
plt.ioff()
plt.show()
