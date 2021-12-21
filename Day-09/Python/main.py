import sys

mat = []
for line in sys.stdin:
    mat.append(list(map(int, line.strip())))

def adj(x, y, mat):
    res = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i + j) ** 2 == 1 and x + i in range(len(mat)) and y + j in range(len(mat[0])):
                res.append(mat[x + i][y + j])
    return res

s = 0
b = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] < min(adj(i, j, mat)):
            s += mat[i][j] + 1
            b.append([i, j])
print("Part 1:", s)

def basin_size(x, y, mat, visited):
    visited[(x, y)] = True
    res = 1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if (i + j) ** 2 == 1 and x + i in range(len(mat)) and y + j in range(len(mat[0])):
                temp = mat[x + i][y + j]
                if (x + i, y + j) not in visited and temp != 9:
                    res += basin_size(x + i, y + j, mat, visited)
    return res

bs = []
for basin in b:
    bs.append(basin_size(*basin, mat, {}))
r = 1
for i in sorted(bs)[-3:]:
    r *= i
print("Part 2:", r)