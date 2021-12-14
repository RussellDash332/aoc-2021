import sys

temp = input().strip()
skip = input()
rule = {}
for line in sys.stdin:
    line = line.strip().split(" -> ")
    rule[line[0]] = line[1]
template = {}
for i in range(len(temp) - 1):
    template[temp[i:i+2]] = template.get(temp[i:i+2], 0) + 1

def evaluate(n):
    c = {}
    for i in template:
        c[i[0]] = c.get(i[0], 0) + template[i]
        c[i[1]] = c.get(i[1], 0) + template[i]
    c[temp[0]] += 1
    c[temp[-1]] += 1
    print(f"Part {n}:", (max(c.values()) - min(c.values())) // 2)

for s in range(40):
    new_t = {}
    for k in template:
        new_t[k[0] + rule[k]] = new_t.get(k[0] + rule[k], 0) + template[k]
        new_t[rule[k] + k[1]] = new_t.get(rule[k] + k[1], 0) + template[k]
    template = new_t
    if s == 9:
        evaluate(1)
evaluate(2)