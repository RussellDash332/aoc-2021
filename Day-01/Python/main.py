import sys

# Part 1, faster
"""
m, ans = float("inf"), 0
for line in sys.stdin:
    if int(line) > m:
        ans += 1
    m = int(line)
print(ans)
"""

m = []
for line in sys.stdin:
    m.append(int(line))

# Part 1
ans = 0
for i in range(1, len(m)):
    if m[i] > m[i-1]:
        ans += 1
print("Part 1:", ans)

# Part 2
ans = 0
for i in range(3, len(m)):
    if m[i] > m[i-3]:
        ans += 1
print("Part 2:", ans)