import sys

d = {}
d2 = {}
for line in sys.stdin:
    l, r = line.split(" -> ")
    (ll, lr), (rl, rr) = l.split(","), r.split(",")
    ll, lr, rl, rr = int(ll), int(lr), int(rl), int(rr)
    if ll == rl:
        for i in range(min(lr, rr), max(lr, rr) + 1):
            d[(ll, i)] = d.get((ll, i), 0) + 1
            d2[(ll, i)] = d2.get((ll, i), 0) + 1
    if lr == rr:
        for i in range(min(ll, rl), max(ll, rl) + 1):
            d[(i, lr)] = d.get((i, lr), 0) + 1
            d2[(i, lr)] = d2.get((i, lr), 0) + 1
    # UL to DR diagonal
    if ll + lr == rl + rr:
        for i in range(min(ll, rl), max(ll, rl) + 1):
            d2[(i, ll + lr - i)] = d2.get((i, ll + lr - i), 0) + 1
    # DL to UR diagonal
    if ll - lr == rl - rr:
        for i in range(min(ll, rl), max(ll, rl) + 1):
            d2[(i, i + lr - ll)] = d2.get((i, i + lr - ll), 0) + 1
print("Part 1:", len(list(filter(lambda x: x > 1, d.values()))))
print("Part 2:", len(list(filter(lambda x: x > 1, d2.values()))))