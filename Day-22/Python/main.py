import sys

def rangeclosed(i, j, *lim):
    if lim:
        return range(max(i, lim[0]), min(j + 1, lim[1] + 1))
    return range(i, j + 1)

def overlap(s1, e1, s2, e2):
    return s2 in range(s1, e1 + 1) or s1 in range(s2, e2 + 1)

def intersect(cube1, cube2):
    mx, my, mz = cube1
    nx, ny, nz = cube2

    if overlap(*mx, *nx) and overlap(*my, *ny) and overlap(*mz, *nz):
        return [
            [max(mx[0], nx[0]), min(mx[1], nx[1])],
            [max(my[0], ny[0]), min(my[1], ny[1])],
            [max(mz[0], nz[0]), min(mz[1], nz[1])]
        ]
    else:
        return None

def subtract(cube1, cube2):
    intersection = intersect(cube1, cube2)
    if not intersection:
        return [cube1]
    else:
        cuboids = []
        [mx1, mx2], [my1, my2], [mz1, mz2] = cube1
        [nx1, nx2], [ny1, ny2], [nz1, nz2] = intersection
        rx = [[mx1, nx1 - 1], [nx1, nx2], [nx2 + 1, mx2]]
        ry = [[my1, ny1 - 1], [ny1, ny2], [ny2 + 1, my2]]
        rz = [[mz1, nz1 - 1], [nz1, nz2], [nz2 + 1, mz2]]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if x * y * z != 1:
                        cuboids.append([rx[x], ry[y], rz[z]])
        return list(filter(lambda x: volume(x), cuboids))

def volume(cube):
    if not cube:
        return 0
    res = 1
    for r in cube:
        res *= (r[1] - r[0] + 1)
    return res

D = {}
cuboids = []
for line in sys.stdin:
    cmd, pos = line.strip().split()
    x, y, z = pos.split(",")
    x1, x2 = list(map(int, x[2:].split("..")))
    y1, y2 = list(map(int, y[2:].split("..")))
    z1, z2 = list(map(int, z[2:].split("..")))

    # Part 1
    for x in rangeclosed(*sorted((x1, x2)), -50, 50):
        for y in rangeclosed(*sorted((y1, y2)), -50, 50):
            for z in rangeclosed(*sorted((z1, z2)), -50, 50):
                D[(x, y, z)] = int(cmd == "on")

    # Part 2
    cuboid = [sorted((x1, x2)), sorted((y1, y2)), sorted((z1, z2))]
    new_cuboids = []
    for c in cuboids:
        new_cuboids.extend(subtract(c, cuboid))
    if cmd == "on":
        new_cuboids.append(cuboid)
    cuboids = new_cuboids
print("Part 1:", sum(D.values()))
print("Part 2:", sum(map(volume, cuboids)))