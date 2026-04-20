f1 = open('career.in', 'r')
data = f1.readlines()
f1.close()

n = int(data[0].strip())
matr = []

for i in range(1, n + 1):
    r = list(map(int, data[i].split()))
    matr.append(r)

for i in range(n - 2, -1, -1):
    for j in range(i + 1):
        if matr[i + 1][j] > matr[i + 1][j + 1]:
            matr[i][j] += matr[i + 1][j]
        else:
            matr[i][j] += matr[i + 1][j + 1]

ans = matr[0][0]

f2 = open('career.out', 'w')
f2.write(str(ans))
f2.close()