"""
По заданному на входе числу 0≤n≤2000 выведите последовательность факториалов: 0!,1!,2!,…,n!
"""

from math import factorial
print(
    *map(
        factorial,
        range(
            int(input()) + 1
        )
    )
)
