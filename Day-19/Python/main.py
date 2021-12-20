import sys

lines = []
for line in sys.stdin:
    lines.append(line.strip())
tmp, scanners = [], []
for x in lines:
    tup = x.split(",")
    if len(tup) == 3:
        tmp.append(tuple(map(int, tup)))
    elif tmp:
        scanners.append(tmp)
        tmp = []
scanners.append(tmp)

# Slow brute forcer but does the job
def gen_all(scanner):
    def helper(scanner):
        tmp1 = [(x, y, z) for x, y, z in scanner]
        tmp2 = [(x, -z, y) for x, y, z in scanner]
        tmp3 = [(x, -y, -z) for x, y, z in scanner]
        tmp4 = [(x, z, -y) for x, y, z in scanner]
        return [tmp1, tmp2, tmp3, tmp4]
    result = helper(scanner)
    result.extend(helper([(-x, z, y) for x, y, z in scanner]))
    result.extend(helper([(y, z, x) for x, y, z in scanner]))
    result.extend(helper([(-y, x, z) for x, y, z in scanner]))
    result.extend(helper([(z, y, -x) for x, y, z in scanner]))

    # Gygilcuf :)
    # Cn niie Lommyff 8 biolm ni lyufcty nbcm mbiofx vy -t, r, -s chmnyux iz -t, r, s.
    # Jlivuvfs hin bcm xus. Ufmi hin nby ijncguf qus iz ayhyluncha uff ilcyhnuncihm, mi.
    result.extend(helper([(-z, x, -y) for x, y, z in scanner]))
    return result

all_oris = list(map(gen_all, scanners))

def get_matches(scanner1, scanner2):
    gen1 = all_oris[scanner1]
    gen2 = all_oris[scanner2]
    res = {}
    for ori1 in range(24):
        for ori2 in range(24):
            d = {}
            for k1 in gen1[ori1]:
                for k2 in gen2[ori2]:
                    triple = tuple(map(lambda x: k1[x] - k2[x], range(3))) + (scanner1*24 + ori1, scanner2*24 + ori2)
                    d[triple] = d.get(triple, 0) + 1
            check = list(filter(lambda x: x[1] >= 12, d.items()))
            if check:
                res[check[0][0][-2]] = (check[0][0][-1], check[0][0][:3])
    return res

mem = {}
overlap = {}
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        if (i, j) not in mem:
            check = get_matches(i, j)
            mem[(i, j)] = check
        else:
            check = mem[(i, j)]
        if check:
            overlap[i] = overlap.get(i, []) + [j]
            overlap[j] = overlap.get(j, []) + [i]

# Run BFS on the overlapping scanners
pos = {0: (0, (0, 0, 0))}
visited = [False] * len(scanners)
q = [0]
while q:
    i = q.pop()
    visited[i] = True
    for j in overlap[i]:
        if not visited[j]:
            if (i, j) not in mem:
                check = get_matches(i, j)
                mem[(i, j)] = check
            else:
                check = mem[(i, j)]
            if pos[i][0] in check:
                q.append(j)
                pos[j] = (check[pos[i][0]][0], tuple(map(sum, zip(check[pos[i][0]][1], pos[i][1]))))

beacons = set(scanners[0])
for i in range(1, len(scanners)):
    for j in all_oris[i][pos[i][0] % 24]:
        beacons.add(tuple(map(sum, zip(j, pos[i][1]))))
print("Part 1:", len(beacons))

manhattan_dists = []
for i in range(len(scanners)):
    for j in range(i + 1, len(scanners)):
        ctr_i = pos[i][1]
        ctr_j = pos[j][1]
        manhattan_dists.append(sum(abs(ctr_i[k] - ctr_j[k]) for k in range(3)))
print("Part 2:", max(manhattan_dists))