from math import *
line = input().strip().split(" ")
px = list(map(int, line[2].replace("x=", "").replace(",", "").split("..")))
py = list(map(int, line[3].replace("y=", "").split("..")))

def check(vx, vy):
    x, y = 0, 0
    while True:
        x, y = x + vx, y + vy
        vx = max(0, vx - 1) # screw negative vx
        vy -= 1
        if x in range(px[0], px[1] + 1) and y in range(py[0], py[1] + 1):
            return True
        if x > px[1] or y < py[0]:
            return False

my = 0
valid = []
for vx in range(int(sqrt(2 * px[0])) - 2, px[1] + 1):
    for vy in range(py[0], 250): # set end range to be big enough
        if check(vx, vy):
            my = max(my, vy)
            valid.append([vx, vy])
print("Part 1:", my * (my + 1) // 2)
print("Part 2:", len(valid))