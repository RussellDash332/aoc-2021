import sys

D = {}
m = []
for line in sys.stdin:
    m.append(list(line.strip()))

for i in range(len(m)):
    for j in range(len(m[0])):
        if m[i][j] != '.':
            D[(i, j)] = ['>', 'v'].index(m[i][j]) + 1

def tick(D, m):
    D1, D2 = {}, {}
    r, c = len(m), len(m[0])
    for i, j in D:
        D1[(i, (j + int(D[(i, j)] == 1 and D.get((i, (j + 1) % c), 0) == 0)) % c)] = D[(i, j)]
    for i, j in D1:
        D2[(((i + int(D1[(i, j)] == 2 and D1.get(((i + 1) % r, j), 0) == 0)) % r, j))] = D1[(i, j)]
    return D2

# Grid-drawing function if needed
def draw(D, m):
    for i in range(len(m)):
        print(str().join(list(map(lambda x: ['.', '>', 'v'][D.get((i, x), 0)], range(len(m[0]))))))
    print()

ctr = 1
while D != tick(D, m):
    D = tick(D, m)
    ctr += 1

print("Part 1:", ctr)
print("Part 2: THE END!")