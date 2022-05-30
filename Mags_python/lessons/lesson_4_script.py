import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as ptch
import seaborn as sns
import numpy.random as rnd  # Генерация случайных чисел


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


cnv = {0: prsi, 1: str, 2: str, 3: prsf, 4: prsf}

S = np.loadtxt('../AUTO21053A.csv', delimiter=';', converters=cnv,
               encoding='utf-8', dtype='O')


def graf(prm1, prm2='price'):
    SEL_COL = [i in (prm1, prm2) for i in S[0, :]]

    S1 = S[:, SEL_COL]

    f = sns.scatterplot(x=S1[1:, 1], y=S1[1:, 0])
    f.set_ylabel(prm2, fontsize='large', fontweight='semibold')
    f.set_xlabel(prm1, fontsize='large', fontweight='semibold')


params = {
    'age': 'Возраст',
    'mlg': 'Пробег'
}

print(f'Параметры на выбор: {params.keys()}')
plt.ion()
fig, ax = plt.subplots(1, 1)
while True:
    a = input('Введите параметр\n')
    graf(a)
    otvet = input("Продолжить? (да/нет) ")
    if otvet == "да":
        ax.clear()
    else:
        break

plt.ioff()
plt.show()
