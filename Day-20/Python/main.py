algo = input().strip()
skip = input()

import sys
D = {}
cnt = 0
for line in sys.stdin:
    tmp = list(line.strip())
    for i in range(len(tmp)):
        D[(cnt, i)] = int(tmp[i] == "#")
    cnt += 1

def adj(i, j):
    return [(i + x, j + y) for x in range(-1, 2) for y in range(-1, 2)]

def bin_to_dec(lst):
    res = 0
    for i in lst:
        res *= 2
        res += i
    return res

min_x, max_x, min_y, max_y = [0, 100]*2
cnt = 0
def enhance():
    global D, min_x, max_x, min_y, max_y, cnt
    new_D = {}
    for i in range(min_x - 1, max_x + 1):
        for j in range(min_y - 1, max_y + 1):
            new_D[(i, j)] = int(algo[bin_to_dec(list(map(lambda x: D.get(x, cnt % 2), adj(i, j))))] == "#")
    D = new_D
    cnt += 1
    min_x, max_x, min_y, max_y = min_x - 1, max_x + 1, min_y - 1, max_y + 1

for _ in range(2):
    enhance()
print("Part 1:", sum(D.values()))
for _ in range(48):
    enhance()
print("Part 2:", sum(D.values()))