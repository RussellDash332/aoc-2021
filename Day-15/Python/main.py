import sys
from heapq import *

m, m2 = [], []
for line in sys.stdin:
    line = list(map(int, line.strip()))
    line2 = line.copy()
    tmp = line.copy()
    m.append(line)
    for i in range(4):
        line2.extend(list(map(lambda x: (x + i + 1) % 9 if (x + i + 1) != 9 else 9, tmp)))
    m2.append(line2)

n = len(m2)
for i in range(4):
    for j in range(n):
        m2.append(list(map(lambda x: (x + i + 1) % 9 if (x + i + 1) != 9 else 9, m2[j])))

# Assuming you can only go right or down
def find(m, n):
    dp = []
    for _ in range(len(m)):
        dp.append([0] * len(m[0]))
    for i in range(1, len(m[0])):
        dp[0][i] = dp[0][i - 1] + m[0][i]
    for i in range(1, len(m)):
        dp[i][0] = dp[i - 1][0] + m[i][0]
    for i in range(1, len(m)):
        for j in range(1, len(m[0])):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + m[i][j]
    print(f"Part {n}:", dp[-1][-1])

# All four sides are possible
def dijkstra(m, n):
    D = [0] * (len(m) * len(m[0]))
    for i in range(1, len(m) * len(m[0])):
        D[i] = 1e9

    def relax(u, v, w):
        if D[u] != 1e9 and D[v] > D[u] + w:
            D[v] = D[u] + w

    def adj(x, y):
        res = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i**2 + j**2 == 1 and x + i in range(len(m)) and y + j in range(len(m[0])):
                    res.append((x + i, y + j))
        return res

    pq = [(0, 0)]
    while list(pq):
        u, d = heappop(pq)
        if d == D[u]:
            for x, y in adj(u // len(m), u % len(m)):
                if D[x * len(m) + y] > D[u] + m[x][y]:
                    relax(u, x * len(m) + y, m[x][y])
                    heappush(pq, (x * len(m) + y, D[x * len(m) + y]))
    print(f"Part {n}:", D[-1])

dijkstra(m, 1)
dijkstra(m2, 2)