import sys

m = []
for line in sys.stdin:
    m.append(list(map(int, line.strip())))

def adj(x, y, mat):
    res = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i, j) != (0, 0) and x + i in range(len(mat)) and y + j in range(len(mat[0])):
                res.append((x + i, y + j))
    return res

def fill(i, j, m):
    for x, y in adj(i, j, m):
        if m[x][y] <= 9:
            m[x][y] += 1
            if m[x][y] == 10:
                fill(x, y, m)

flashes = 0
flash = 0
i = 0
while flash != len(m) * len(m[0]):
    flash = 0
    for j in range(len(m)):
        for k in range(len(m[0])):
            m[j][k] += 1
            if m[j][k] == 10:
                fill(j, k, m)
    for j in range(len(m)):
        for k in range(len(m[0])):
            m[j][k] = min(m[j][k], 10) % 10
    for j in range(len(m)):
        tmp = sum(map(lambda x: 1 if x == 0 else 0, m[j]))
        flashes += tmp
        flash += tmp
    if i == 99:
        print("Part 1:", flashes)
    i += 1
print("Part 2:", i)