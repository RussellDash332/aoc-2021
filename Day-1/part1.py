import sys

m = []
for line in sys.stdin:
    m.append(int(line))

ans = 0
for i in range(1, len(m)):
    if m[i] > m[i-1]:
        ans += 1
print(ans)