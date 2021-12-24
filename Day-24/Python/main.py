import sys, z3

cmds = []
for line in sys.stdin:
    cmds.append(line.strip().split())

# Naive checker
def check_monad(k):
    ctr, w, x, y, z = 0, [0], [0], [0], [0]
    d = {'w': w, 'x': x, 'y': y, 'z': z}
    for cmd in cmds:
        if cmd[0] == "inp":
            d[cmd[1]][0] = int(k[ctr])
            ctr += 1
        elif cmd[0] == "add":
            try:
                d[cmd[1]][0] += int(cmd[2])
            except:
                d[cmd[1]][0] += d[cmd[2]][0]
        elif cmd[0] == "mul":
            try:
                d[cmd[1]][0] *= int(cmd[2])
            except:
                d[cmd[1]][0] *= d[cmd[2]][0]
        elif cmd[0] == "div":
            try:
                d[cmd[1]][0] //= int(cmd[2])
            except:
                d[cmd[1]][0] //= d[cmd[2]][0]
        elif cmd[0] == "mod":
            try:
                d[cmd[1]][0] %= int(cmd[2])
            except:
                d[cmd[1]][0] %= d[cmd[2]][0]
        else:
            try:
                d[cmd[1]][0] = int(d[cmd[1]][0] == int(cmd[2]))
            except:
                d[cmd[1]][0] = int(d[cmd[1]][0] == d[cmd[2]][0])
    return z[0]

# Slower because directly uses 24.in
def slow_z3():
    w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14 = z3.Ints(' '.join(['w' + str(i + 1) for i in range(14)]))

    ctr, w, x, y, z = 0, [0], [0], [0], [0]
    d = {'w': w, 'x': x, 'y': y, 'z': z}
    for i in range(14):
        d['w' + str(i + 1)] = w

    for cmd in cmds:
        if cmd[0] == "inp":
            d[cmd[1]][0] = eval(f'w{ctr + 1}')
            ctr += 1
        else:
            right = cmd[2]
            if right == "w":
                right = f'w{ctr}'
            if cmd[0] == "add":
                try:
                    d[cmd[1]][0] += int(right)
                except:
                    d[cmd[1]][0] += d[right][0]
            elif cmd[0] == "mul":
                try:
                    d[cmd[1]][0] *= int(right)
                except:
                    d[cmd[1]][0] *= d[right][0]
            elif cmd[0] == "div":
                try:
                    d[cmd[1]][0] /= int(right)
                except:
                    d[cmd[1]][0] /= d[right][0]
            elif cmd[0] == "mod":
                try:
                    d[cmd[1]][0] %= int(right)
                except:
                    d[cmd[1]][0] %= d[right][0]
            else:
                try:
                    d[cmd[1]][0] = If(d[cmd[1]][0] == int(right), 1, 0)
                except:
                    d[cmd[1]][0] = If(d[cmd[1]][0] == d[right][0], 1, 0)

    bools = [z[0] == 0]
    for i in range(14):
        bools.append(eval(f"w{i + 1} >= 1"))
        bools.append(eval(f"w{i + 1} <= 9"))

    val = sum([10**(13 - i) * eval(f"w{i + 1}") for i in range(14)])

    s = z3.Optimize()
    for con in bools:
        s.add(con)
    s.maximize(val)
    assert s.check() == z3.sat
    print("Part 1:", s.model().eval(val))

    s = z3.Optimize()
    for con in bools:
        s.add(con)
    s.minimize(val)
    assert s.check() == z3.sat
    print("Part 2:", s.model().eval(val))

# We can actually simplify some operations as seen in 24_modified.in
# For every k, z_k's second term is actually y_k
w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14 = z3.Ints(' '.join(['w' + str(i + 1) for i in range(14)]))
x0, z0 = 0, 0

x1 = (z0 % 26 + 11 != w1)
z1 = z0 * (25 * x1 + 1) + (w1 + 5) * x1

x2 = (z1 % 26 + 13 != w2)
z2 = z1 * (25 * x2 + 1) + (w2 + 5) * x2

# Clash with package name, didn't want to use `from z3 import *` to avoid solve method confusion
x3 = (z2 % 26 + 12 != w3)
zee3 = z2 * (25 * x3 + 1) + (w3 + 1) * x3

x4 = (zee3 % 26 + 15 != w4)
z4 = zee3 * (25 * x4 + 1) + (w4 + 15) * x4

x5 = (z4 % 26 + 10 != w5)
z5 = z4 * (25 * x5 + 1) + (w5 + 2) * x5

x6 = (z5 % 26 - 1 != w6)
z6 = z5 / 26 * (25 * x6 + 1) + (w6 + 2) * x6

x7 = (z6 % 26 + 14 != w7)
z7 = z6 * (25 * x7 + 1) + (w7 + 5) * x7

x8 = (z7 % 26 - 8 != w8)
z8 = z7 / 26 * (25 * x8 + 1) + (w8 + 8) * x8

x9 = (z8 % 26 - 7 != w9)
z9 = z8 / 26 * (25 * x9 + 1) + (w9 + 14) * x9

x10 = (z9 % 26 - 8 != w10)
z10 = z9 / 26 * (25 * x10 + 1) + (w10 + 12) * x10

x11 = (z10 % 26 + 11 != w11)
z11 = z10 * (25 * x11 + 1) + (w11 + 7) * x11

x12 = (z11 % 26 - 2 != w12)
z12 = z11 / 26 * (25 * x12 + 1) + (w12 + 14) * x12

x13 = (z12 % 26 - 2 != w13)
z13 = z12 / 26 * (25 * x13 + 1) + (w13 + 13) * x13

x14 = (z13 % 26 - 13 != w14)
z14 = z13 / 26 * (25 * x14 + 1) + (w14 + 6) * x14

bools = [z14 == 0]
for i in range(14):
    bools.append(eval(f"w{i + 1} >= 1"))
    bools.append(eval(f"w{i + 1} <= 9"))
val = sum([10**(13 - i) * eval(f"w{i + 1}") for i in range(14)])

def solve(n):
    s = z3.Optimize()
    for con in bools:
        s.add(con)
    if n % 2:
        s.maximize(val)
    else:
        s.minimize(val)
    assert s.check() == z3.sat
    print(f"Part {n}:", s.model().eval(val))

solve(1)
solve(2)