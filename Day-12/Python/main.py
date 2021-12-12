import sys

g = {}
for line in sys.stdin:
    line = line.strip().split("-")
    g[line[0]] = g.get(line[0], []) + [line[1]]
    g[line[1]] = g.get(line[1], []) + [line[0]]

def num_paths(s, sm, g, b):
    if s == "end":
        # print(b + [s])
        return 1
    elif s in sm:
        return 0
    else:
        p = 0
        for i in g.get(s):
            if i != 'start':
                if s.islower():
                    p += num_paths(i, sm + [s], g, b + [s])
                else:
                    p += num_paths(i, sm, g, b + [s])
        return p

def num_paths2(s, sm, g, b):
    if s == "end":
        # print(b + [s])
        return 1
    elif len(list(filter(lambda x: x >= 2, sm.values()))) >= 2 or \
        len(list(filter(lambda x: x > 2, sm.values()))) != 0:
        return 0
    else:
        p = 0
        for i in g.get(s):
            if i != 'start':
                if s.islower():
                    d = sm.copy()
                    d[s] = d.get(s, 0) + 1
                    if len(list(filter(lambda x: x >= 2, d.values()))) < 2 and \
                        len(list(filter(lambda x: x > 2, d.values()))) == 0:
                        p += num_paths2(i, d, g, b + [s])
                else:
                    p += num_paths2(i, sm, g, b + [s])
        return p

print("Part 1:", num_paths('start', [], g, []))
print("Part 2:", num_paths2('start', {}, g, []))