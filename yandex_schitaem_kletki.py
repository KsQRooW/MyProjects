def add_dict(myDict, key, a):
    if myDict.get(key, -1) == -1:
        myDict[key] = (a,)
    else:
        myDict[key] = myDict[key] + (a,)


def add_picture(myDict, reverse=False):
    if not reverse:
        # key - значение y_i в picture
        for key in myDict:
            for i in range(0, len(myDict[key]), 2):
                # j - значение x_i в picture
                step = -1 if myDict[key][i] > myDict[key][i + 1] else 1
                for j in range(myDict[key][i] + step, myDict[key][i + 1], step):  # если (2, 6) -> хотим получить 3, 4, 5
                    picture[j][key] = 2
    else:
        # key - значение y_i в picture
        for key in myDict:
            for i in range(0, len(myDict[key]), 2):
                # j - значение x_i в picture
                step = -1 if myDict[key][i] > myDict[key][i + 1] else 1
                for j in range(myDict[key][i] + step, myDict[key][i + 1], step):  # если (2, 6) -> хотим получить 3, 4, 5
                    picture[key][j] = 2


n, m = map(int, input().split())
k = int(input())
x = {}
y = {}
picture = [[0] * n for i in range(m)]
for i in range(k):
    x_i, y_i = map(lambda t: int(t) - 1, input().split())
    add_dict(x, x_i, y_i)
    add_dict(y, y_i, x_i)
    picture[y_i][x_i] = 1
# picture.reverse()

# print('x:', x)
# print('y:', y)

# key - значение y_i в picture
add_picture(x)
add_picture(y, True)

# print(*picture[::-1], sep='\n')
