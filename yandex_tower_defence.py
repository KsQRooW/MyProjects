n, m = input().split()
plita = list(map(int, input().split()))
plechi = list(map(int, input().split()))
plita_soln = []

max_pl = plita[-1]
plita_soln.append(max_pl)
for i in range(len(plita) - 2, -1, -1):
    z = plita[i] - max_pl
    if plita[i] >= max_pl:
        max_pl = plita[i]
    if z > 0:
        plita_soln.append(z)

plita_soln.sort()
plechi.sort()

i = len(plechi) - 1
j = len(plita_soln) - 1
k = 0
while i != -1 and j != -1:
    if plechi[i] <= plita_soln[j]:
        k += 1
        i -= 1
        j -= 1
    else:
        i -= 1
print(k)
