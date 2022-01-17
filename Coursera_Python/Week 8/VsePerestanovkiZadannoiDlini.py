"""
По данному числу N выведите все перестановки чисел от 1 до N в лексикографическом порядке.
"""

from itertools import permutations

print(
    *map(
        ''.join,
        permutations(
            map(
                str,
                range(1,
                      int(input()) + 1
                      )
            )
        )
    ),
    sep='\n'
)
