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
