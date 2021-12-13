import sys

p = []
cmd = []
pts = True
for line in sys.stdin:
    line = line.strip()
    if not line:
        pts = False
        continue
    if pts:
        line = line.split(",")
        p.append([int(line[0]), int(line[1])])
    else:
        line = line.split("=")
        cmd.append([line[0][-1], int(line[1])])
r = max(map(lambda x: x[1], p)) + 1
c = max(map(lambda x: x[0], p)) + 1
for ax, n in cmd:
    new_p = {}
    for px, py in p:
        if ax == 'x':
            new_p[(n - abs(px - n), py)] = True
        else:
            new_p[(px, n - abs(py - n))] = True
    p = new_p
    if ax == 'x':
        c = max(map(lambda x: x[0], p.keys())) + 1
    else:
        r = max(map(lambda x: x[1], p.keys())) + 1
    if (ax, n) == tuple(cmd[0]):
        print("Part 1:", len(p))

final_m = []
for _ in range(r):
    final_m.append(["."] * c)
for px, py in p:
    final_m[py][px] = "#"
print("Part 2:")
for row in final_m:
    print(str().join(row))