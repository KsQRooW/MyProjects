def add_dict(myDict, key, a):
    if myDict.get(key, -1) == -1:
        myDict[key] = (a,)
    else:
        myDict[key] = myDict[key] + (a,)


count_0 = 0


def help_picture(picture, key1, j1, sp=True):
    global count_0
    if sp:
        picture[j1][key1] = 2
        count_0 += 1
    else:
        picture[key1][j1] = 2
        count_0 += 1


def add_picture(my_dict, reverse=True):
    # key - значение y_i в picture
    for key in my_dict:
        for i in range(0, len(my_dict[key]), 2):
            # j - значение x_i в picture
            step = -1 if my_dict[key][i] > my_dict[key][i + 1] else 1
            for j in range(my_dict[key][i] + step, my_dict[key][i + 1], step):  # если (2, 6) -> хотим получить 3, 4, 5
                help_picture(picture, key, j, reverse)


def full_cells(picture):
    counter_full_cells = 0
    for i in range(1, len(picture)):
        flag = False
        change_flag = False
        for j in range(1, len(picture[0])):
            if flag:
                if picture[i][j] == 0:
                    picture[i][j] = 3
                    counter_full_cells += 1
                    change_flag = True
                elif change_flag:
                    flag = False
                elif picture[i][j + 1:].count(1) == 0 and picture[i][j + 1:].count(2) == 0:
                    flag = False
                elif picture[i][j + 1:].count(1) + picture[i][j + 1:].count(2) >= 2:
                    flag = False
            elif picture[i][j] != 0:
                flag = True
                change_flag = False
    return counter_full_cells


def corners(pic):
    count_internal_corners = 0
    count_outside_corners = 0
    for i in range(1, len(pic) - 1):
        for j in range(1, len(pic[i]) - 1):
            if pic[i][j] == 1:
                if pic[i - 1][j] == 3 or pic[i + 1][j] == 3 or pic[i][j - 1] == 3 or pic[i + 1][j] == 3:
                    count_internal_corners += 1
                else:
                    count_outside_corners += 1
    return str(count_outside_corners) + " " + str(count_internal_corners)


n, m = map(int, input().split())
k = int(input())
x = {}
y = {}
picture = [[0] * (n + 2) for i in range(m + 2)]
for i in range(k):
    x_i, y_i = map(lambda t: int(t), input().split())
    add_dict(x, x_i, y_i)
    add_dict(y, y_i, x_i)
    picture[y_i][x_i] = 1
# picture.reverse()

# print('x:', x)
# print('y:', y)
# key - значение y_i в picture
add_picture(x)
add_picture(y, False)
print(full_cells(picture), count_0, corners(picture))
# print(*picture[::-1], sep='\n')
# print(*picture, sep='\n')
