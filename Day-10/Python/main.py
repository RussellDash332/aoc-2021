import sys

err, com = 0, []
end_brackets = ')]}>'
open_brackets = '([{<'
errmap = dict(zip(end_brackets, [3, 57, 1197, 25137]))
commap = dict(zip(end_brackets, [1, 2, 3, 4]))
match = dict(zip(end_brackets, open_brackets))
rev_match = dict(zip(open_brackets, end_brackets))
incomplete = []
for line in sys.stdin:
    line = line.strip()
    stack = []
    corrupt = False
    for i in line:
        if i in errmap:
            if match[i] != stack.pop():
                err += errmap[i]
                corrupt = True
                break
        else:
            stack.append(i)
    if stack and not corrupt:
        incomplete.append(stack)
print("Part 1:", err)

incomplete = list(map(lambda x: list(map(lambda y: rev_match[y], x[::-1])), incomplete))
for i in incomplete:
    score = 0
    for j in i:
        score *= 5
        score += commap[j]
    com.append(score)
print("Part 2:", sorted(com)[len(com) // 2])