import os
import sys
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import seaborn as sns
import numpy.random as rnd  # Генерация случайных чисел

# Настройка для всех рисунков
sns.set_theme(context='notebook', style='darkgrid', palette='deep',
              font='sans-serif', font_scale=1, color_codes=False, rc=None)

# context — параметры контекста, влияет на размер меток, линий и других
# элементов, но не на общий стиль. Контекст: notebook, paper, talk, poster;
# style — стиль осей: darkgrid (серый фон с сеткой),
# whitegrid (белый фон с сеткой), dark (серый фон без сетки),
# white (белый фон без сетки), ticks;
# palette — цветовая палитра: deep, muted, bright, pastel, dark, colorblind,
# а так же палитры из matplotlib;
# font — шрифт текста;
# font_scale — масштабирование размера текста.
# color_codes - если True, то коды цветов переопределяются по палитре
# rc - словарь для переопределения параметров

# v = 5/7
# x = np.linspace(0, 14, 100)
# y = np.sin(2*np.pi*v*x)
# plt.figure(figsize=(15, 9))
# plt.subplots_adjust(wspace=0.2, hspace=0.2)
# for i, cnt in enumerate(['darkgrid', 'whitegrid', 'dark', 'white', 'ticks']):
#     sns.set_theme(style=cnt)  # Устанавливаем стиль
#     plt.subplot(3, 2, i+1)
#     plt.plot(x, y)
#     plt.title(cnt)

# # Палитры
# sns.palplot(sns.color_palette()) # Палитра по умолчанию
# sns.palplot(sns.color_palette('colorblind'))
# # Создание палитры цветов (RGBA) - прозрачность, 1 - не прозрачный
# clr = [(0.8, 0.0, 0.0, 1), (0.0, 0.5, 0.0, 0.5), (0.0, 0.0, 0.3, 0.25)]
# my = sns.color_palette(palette=clr)
# sns.palplot(my, size=0.5)
#
# # Создание палитры на основе базового цвета
# sns.palplot(sns.dark_palette("orange", n_colors=10))
# sns.palplot(sns.light_palette("orange", n_colors=10))


# # Временная настройка контекстный менеджер
# with sns.plotting_context("paper"), sns.axes_style("ticks"):
#     X = np.array([1, 2, 3])
#     Y = np.array([-1, 4, 10])
#     g = sns.barplot(x=X, y=Y, palette='dark')

# # BARPLOT обычный
# X = np.array([1, 2, 3])
# Y = np.array([5, 4, 10])
# g = sns.barplot(x=X, y=Y, palette='dark')

# # BARPLOT с оценкой
# num = 300
# thr = 0.7
# m1 = -2
# s1 = 1
# m2 = 2
# s2 = 2
# X1 = s1*rnd.randn(num) + m1
# X2 = s2*rnd.randn(num) + m2
# SEL = rnd.uniform(0, 1, num)
# Y = np.where(SEL<thr, X1, X2)
# Z = np.where(SEL<thr, 'a', 'b')
# # ci - доверительный интервал
# g = sns.barplot(x=Z, y=Y, estimator=np.mean, ci='sd', palette='colorblind')

# # ........... Диаграмма рассеивания - scatterplot ............

# # 1
# c1 = (1,0,0)
# c2 = (0,1,0)
# c3 = (0,0,1)
# c4 = (0.5, 0.5, 0.5)
# c = [c1, c2, c3, c4]
# #c = [1, 2, 3, 4]
# d = [100, 200, 300, 400]
# x = np.arange(4.0)
# y = x**2
# plt.scatter(x, y, c=c, s=d)
# plt.show()

# # 2
# num = 50
# x = rnd.uniform(-1, 2, num)
# v = rnd.randn(num)
# y1 = 2.0 + 3.0*x + v
# y2 = 1.0 + 2.0*x + v
# cm = 'r'
# cf = 'b'
# plt.scatter(x, y1, c=cm, marker = '+', label='male')
# plt.scatter(x, y2, c=cf, label='female')
# plt.legend(loc='best')

# # 3 Выгрузка из БД
# num = 50
# gnd = rnd.choice(["m", "f"], num)
# x = rnd.uniform(-1, 2, num)
# v = rnd.randn(num)
# y = 2.0 + 3.0*x + v
# cm = 'r'
# cf = 'b'
# c = np.where(gnd == "m" ,cm, cf)
# plt.scatter(x, y, c=c)

plt.show()
