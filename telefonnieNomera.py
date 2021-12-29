doc = open('Coursera_Python/7%_Barier.txt')
flag = True
x = ''
for a in doc:
    a = a.replace('-', '')
    a = a.replace('(', '')
    a = a.replace(')', '').rstrip()
    if flag:
        if len(a) == 11:
            a = '7' + a[1:]
        if len(a) == 12:
            a = a.replace('+', '')
        if len(a) == 7:
            a = '7495' + a
        x = a
        flag = False
    else:
        k = len(a)
        if len(a) == 12:
            a = a.replace('+', '')
        elif len(a) == 7:
            a = '7495' + a
        elif len(a) == 11:
            a = '7' + a[1:]
        if a == x:
            print('YES')
        else:
            print('NO')
