seq = list(map(int, input().split(",")))
skip = input()

import sys
bingos = []
bingo = []

for line in sys.stdin:
    r = list(map(int,line.split()))
    if not r:
        bingos.append(bingo)
        bingo = []
    else:
        bingo.append(r)
bingos.append(bingo)

def transpose(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]

def is_bingo(m):
    for row in m:
        if sum(row) == 0:
            return True
    for row in transpose(m):
        if sum(row) == 0:
            return True
    # assuming m is a square matrix
    return sum(m[i][i] for i in range(len(m))) == 0 or \
        sum(m[i][-i-1] for i in range(len(m))) == 0

part1_done = False
for k in seq:
    for b in bingos:
        for i in range(len(b)):
            b[i] = list(map(lambda x: 0 if x == k else x, b[i]))
        if is_bingo(b):
            if not part1_done:
                print("Part 1:", k * sum(map(sum, b)))
                part1_done = True
            if len(bingos) == 1:
                print("Part 2:", k * sum(map(sum, b)))
                sys.exit(0)
    bingos = list(filter(lambda x: not is_bingo(x), bingos))