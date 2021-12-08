import sys

left, right = [], []
for line in sys.stdin:
    line = line.strip().split(" | ")
    left.append(line[0].split())
    right.append(line[1].split())
print("Part 1:", sum(map(lambda x: len(list(filter(lambda y: len(y) in [2, 3, 4, 7], x))), right)))

for i in range(len(right)):
    mapping = {}
    for j in left[i]:
        if len(j) == 2:
            one = str().join(sorted(j))
            mapping[one] = '1'
        elif len(j) == 3:
            seven = str().join(sorted(j))
            mapping[seven] = '7'
        elif len(j) == 4:
            four = str().join(sorted(j))
            mapping[four] = '4'
        elif len(j) == 7:
            eight = str().join(sorted(j))
            mapping[eight] = '8'
    for j in left[i]:
        if len(j) == 6:
            if set(four).issubset(set(j)):
                nine = str().join(sorted(j))
                mapping[nine] = '9'
            elif set(one).issubset(set(j)):
                zero = str().join(sorted(j))
                mapping[zero] = '0'
            else:
                six = str().join(sorted(j))
                mapping[six] = '6'
    for j in left[i]:
        if len(j) == 5:
            if not set(zero).difference(set(six)).issubset(set(j)):
                mapping[str().join(sorted(j))] = '5'
            elif set(one).issubset(set(j)):
                mapping[str().join(sorted(j))] = '3'
            else:
                mapping[str().join(sorted(j))] = '2'
    right[i] = int(str().join(list(map(lambda x: mapping[str().join(sorted(x))], right[i]))))
print("Part 2:", sum(right))