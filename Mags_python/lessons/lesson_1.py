import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import seaborn as sns
import numpy.random as rnd  # Генерация случайных чисел

# # Столбчатая диаграмма
# # 1
names = ['А', 'Б', 'В']
values = [1, 30, 10]
clr = ['r', 'g', 'b']
plt.bar(names, values, color=clr)
plt.show()

# # 2 Категоризированный график
# X = np.array([1,3,5])
# Offset = 0.4
# Y = [1,2,3]
# Z = [2,3,4]
# plt.bar(X - Offset, Y) # offset of -0.4
# plt.bar(X + Offset, Z) # offset of  0.4
# plt.show()

# # 3 Ручная простановка подписей
# X = ['A','B','C']
# Y = [1,2,3]
# Z = [2,3,4]
# _X = np.arange(len(X))
# Width = 0.4
# plt.bar(_X - 0.2, Y, Width)
# plt.bar(_X + 0.2, Z, Width)
# plt.xticks(_X, X) # set labels manually
# plt.show()

# # 4 Размещение нескольких графиков
# cm = 1/2.54 # Размер в см
# fig, ax = plt.subplots(2, 1, figsize=(5*cm, 10*cm))
# fig.subplots_adjust(wspace=0.5, hspace=0.5)
# names = ['А', 'Б', 'В']
# values = [1, 30, 10]
# #clr = ['r', 'g', 'b']
# clr = [(0.5,0,0), (0,1,0), (0,0,0.8)]
# ax[0].bar(names, values, color=clr)
# # Качественные данные
# n = 300
# p = [0.2, 0.5, 0.3]
# Z = rnd.choice(["a", "b", "c"], n, replace=True, p=p)
# U = np.unique(Z, return_counts=True)
# ax[1].bar(U[0], U[1])
# plt.show()
