import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

B = pd.Series([4, 7, -5, 3])
print(B, '\n')

D1 = B.copy()
D1.index = ["ы", "й", "я", "я"]

W = {'A': 35000, 'B': 71000, 'C': 16000, 'D': 5000}
A = pd.Series(W)

print(B.dtype)
D1 = B.copy()
D1[D1 < 0] = np.nan
print(D1)  # float64

F1 = pd.DataFrame([[1, 2], [3, 4]])
print(F1.index, F1.columns)  # Два индекса
F1.dtypes

W1 = {'year': [2000, 2001, 2002, 2001, 2002],
      'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
F2 = pd.DataFrame(W1, index=['A', 'A', 'A', 'B', 'B'])
