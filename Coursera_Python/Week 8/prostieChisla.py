"""
Выведите все простые числа на отрезке [2;n].
"""

from math import sqrt

print(
    *filter(
        lambda x: not any(
            map(
                lambda y: x % y == 0,
                range(
                    2,
                    int(sqrt(x)) + 1)
            )
        ),
        range(
            2,
            int(input()) + 1)
    )
)
