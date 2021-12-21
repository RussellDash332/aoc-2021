p1, p2 = int(input().strip()[-1]), int(input().strip()[-1])

def wrap(a, mod):
    if a % mod == 0:
        return mod
    return a % mod

def play(dice, p1, p2):
    s1, s2, cnt = 0, 0, 0
    while s1 < 1000 and s2 < 1000:
        p1 = wrap(p1 + 3 * dice, 10)
        dice = wrap(dice + 3, 100)
        cnt, s1 = cnt + 3, s1 + p1
        if s1 >= 1000:
            break
        p2 = wrap(p2 + 3 * dice, 10)
        dice = wrap(dice + 3, 100)
        cnt, s2 = cnt + 3, s2 + p2
    return (s1, s2, cnt)
res = play(2, p1, p2)
print("Part 1:", min(res[:2]) * res[-1])

mem = {}
cts = {}
for i in range(3):
    for j in range(3):
        for k in range(3):
            cts[i + j + k + 3] = cts.get(i + j + k + 3, 0) + 1

LIMIT = 21
def play2(p1, p2, s1, s2, turn):
    if (p1, p2, s1, s2, turn) in mem:
        return mem[(p1, p2, s1, s2, turn)]
    stats = {0: 0, 1: 0}
    if s1 >= LIMIT or s2 >= LIMIT:
        stats[int(s2 > s1)] += 1
        mem[(p1, p2, s1, s2, turn)] = stats
        return stats

    for die in range(3, 10):
        if not turn:
            new_p1 = wrap(p1 + die, 10)
            tmp = play2(new_p1, p2, s1 + new_p1, s2, 1 - turn)
        else:
            new_p2 = wrap(p2 + die, 10)
            tmp = play2(p1, new_p2, s1, s2 + new_p2, 1 - turn)
        for i in range(2):
            stats[i] += cts[die] * tmp[i]
    mem[(p1, p2, s1, s2, turn)] = stats
    return stats
res2 = play2(p1, p2, s1=0, s2=0, turn=0)
print("Part 2:", max(res2.values()))