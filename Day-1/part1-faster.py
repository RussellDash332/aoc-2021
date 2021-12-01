import sys

m, ans = float("inf"), 0
for line in sys.stdin:
    if int(line) > m:
        ans += 1
    m = int(line)
print(ans)