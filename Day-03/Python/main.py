def bin_to_dec(b):
    res = 0
    for i in b:
        res *= 2
        res += int(i)
    return res

import sys
bits, tmp = [], []
for line in sys.stdin:
    bits.append(line.strip())

# Part 1
for line in bits:
    if not tmp:
        tmp = list(map(int, line))
    else:
        for i in range(len(line)):
            tmp[i] += int(line[i])
n = len(bits)
gam = str().join(list(map(lambda x: str(int(x > n/2)), tmp)))
eps = str().join(list(map(lambda x: str(int(x < n/2)), tmp)))
print("Part 1:", bin_to_dec(gam) * bin_to_dec(eps))

# Part 2
b = len(bits[0])
bits2 = bits.copy()
for i in range(b):
    if len(bits) == 1:
        break
    freq = [0, 0]
    for bit in bits:
        freq[int(bit[i])] += 1
    if freq[0] > freq[1]:
        bits = list(filter(lambda x: x[i] == "0", bits))
    else:
        bits = list(filter(lambda x: x[i] == "1", bits))
for i in range(b):
    if len(bits2) == 1:
        break
    freq = [0, 0]
    for bit in bits2:
        freq[int(bit[i])] += 1
    if freq[0] > freq[1]:
        bits2 = list(filter(lambda x: x[i] == "1", bits2))
    else:
        bits2 = list(filter(lambda x: x[i] == "0", bits2))
print("Part 2:", bin_to_dec(bits[0]) * bin_to_dec(bits2[0]))