import sys

m = []
for line in sys.stdin:
    m.append(int(line))

ans = 0
for i in range(3, len(m)):
    if m[i] > m[i-3]:
        ans += 1
print(ans)