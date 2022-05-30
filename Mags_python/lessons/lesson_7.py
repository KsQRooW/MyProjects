import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

cars = pd.read_excel('AUTO21053A.xlsx')
cars_col: DataFrame = cars.loc[:, cars.dtypes != 'O']
cars_kach: DataFrame = cars.loc[:, cars.dtypes == 'O']

# cars.hist(grid=True, density=True, bins='fd', orientation='vertical')
# 'fd', 'scott', 'sturges'

# ax = lambda x: plt.subplot(1, 2, x)

while True:
    i1 = input(f'Выберите столбец из списка: {" ".join(cars_col)}\n')
    cars_col = cars_col.drop(columns=i1)
    i2 = input(f'Выберите еще один столбец из списка: {" ".join(cars_col)}\n')
    j = input(f'Выберите столбец из списка для категоризации: {" ".join(cars_kach)}\n')
    # a = cars[i].hist(grid=True, density=True, bins='scott', orientation='vertical', ax=ax(1)).set(xlabel=i)
    cars.groupby(j).plot.scatter(x=i1, y=i2, c='red')
    cars.groupby(j).plot.scatter(x=i1, y=i2, c='blue')
    # b = cars[j].hist(grid=True, density=True, bins='scott', orientation='vertical', ax=ax(2)).set(xlabel=j)
    # plt.subplots_adjust(bottom=0.1, wspace=0.5)
    plt.show()
    break

# CARS['price'].hist(grid=True, by=CARS['music'], density=True, bins='fd',
#                    orientation='vertical')
#
# # Можно использовать списки
# CARS.boxplot(grid=True, column='price', by='music', notch=True,
#                         showmeans=True, whis=1.5, vert=True, bootstrap=100)

# CARS.plot.scatter('mlg', 'price', s = 300) # s - диаметр, c - цвет
# plt.title('Зависимость цены от пробега')
