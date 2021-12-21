import sys

x, y1, y2 = 0, 0, 0
for line in sys.stdin:
    cmd, d = line.split()
    d = int(d)
    if cmd == "forward":
        x += d
        y2 += y1 * d
    elif cmd == "up":
        y1 -= d
    else:
        y1 += d
print("Part 1:", x * y1)
print("Part 2:", x * y2)