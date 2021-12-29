from functools import reduce

print(*map(lambda y: y.count('1') % 2, map(str, reduce(zip, map(lambda x: input().split(), range(int(input())))))))
