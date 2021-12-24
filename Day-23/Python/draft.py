import sys

m = []
for line in sys.stdin:
    tmp = list(line.strip())
    pad = ['X'] * ((13 - len(tmp)) // 2)
    m.append(pad + tmp + pad)

def finished(m):
    return gen_pos(m) == [(i, 2*j + 3) for j in range(4) for i in range(2, len(m) - 1)]

def gen_pos(m):
    # [A..AB..BC..CD..D]
    return sorted([(i, 2*j + 3) for j in range(4) for i in range(2, len(m) - 1)], key=lambda x: m[x[0]][x[1]])

def gen_pos_with_dots(m):
    return gen_pos(m) + [(1, i) for i in range(1, 12)]

def make_config(abcd_pos):
    num_pods = len(abcd_pos) // 4
    res = [list('#' * 13), list('#' + '.' * 11 + '#')]
    res.append(list('###.#.#.#.###'))
    for _ in range(num_pods - 1):
        res.append(list('XX#.#.#.#.#XX'))
    res.append(list('XX#########XX'))
    for k in range(len(abcd_pos)):
        x, y = abcd_pos[k]
        res[x][y] = 'ABCD'[k // num_pods]
    return res

def subtract(lst, k):
    res = []
    for i in lst:
        if i != k:
            res.append(lst)
    return res, k

# Draft Part 1
pos = gen_pos_with_dots(m)
states = []

# Draft Part 2
m[3:3] = [list('XX#D#C#B#A#XX'), list('XX#D#B#A#C#XX')]