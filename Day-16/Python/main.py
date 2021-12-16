def bit_to_dec(bit):
    res = 0
    for b in bit:
        res *= 2
        res += int(b == "1")
    return res
hex_to_bit = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

bits = []
hexa = input().strip()
for h in hexa:
    bits.extend(hex_to_bit[h])

total_v = 0
def read_literal(bits, start):
    pos = start
    lit = []
    while bits[pos] != "0":
        lit.extend(bits[pos+1:pos+5])
        pos += 5
    lit.extend(bits[pos+1:pos+5])
    return (pos + 5, bit_to_dec(lit))

# Decided to wrap this in a function so can try out for multiple inputs
def parse(bits):
    v = bit_to_dec(str().join(bits[:3]))
    t = bit_to_dec(str().join(bits[3:6]))

    def keep_reading(pos):
        global total_v
        v = bit_to_dec(str().join(bits[pos:pos+3]))
        t = bit_to_dec(str().join(bits[pos+3:pos+6]))
        total_v += v
        lits = []

        if t == 4:
            return read_literal(bits, pos+6)
        else:
            i = bits[pos+6]
            if i == "0":
                spl = bit_to_dec(str().join(bits[pos+7:pos+22]))
                pos2 = pos + 22
                while pos2 != pos + 22 + spl:
                    pos2, val = keep_reading(pos2)
                    lits.append(val)
            else:
                spn = bit_to_dec(str().join(bits[pos+7:pos+18]))
                pos2 = pos + 18
                for _ in range(spn):
                    pos2, val = keep_reading(pos2)
                    lits.append(val)

            if t == 0:
                return pos2, sum(lits)
            elif t == 1:
                prod = 1
                for l in lits:
                    prod *= l
                return pos2, prod
            elif t == 2:
                return pos2, min(lits)
            elif t == 3:
                return pos2, max(lits)
            elif t == 5:
                return pos2, int(lits[0] > lits[1])
            elif t == 6:
                return pos2, int(lits[0] < lits[1])
            return pos2, int(lits[0] == lits[1])

    global total_v
    total_v += v
    lits = []

    if t == 4:
        return read_literal(bits, 6)[1]
    else:
        i = bits[6]
        if i == "0":
            spl = bit_to_dec(str().join(bits[7:22]))
            pos = 22
            while pos != 22 + spl:
                pos, val = keep_reading(pos)
                lits.append(val)
        else:
            spn = bit_to_dec(str().join(bits[7:18]))
            pos = 18
            for _ in range(spn):
                pos, val = keep_reading(pos)
                lits.append(val)

        if t == 0:
            return sum(lits)
        elif t == 1:
            prod = 1
            for l in lits:
                prod *= l
            return prod
        elif t == 2:
            return min(lits)
        elif t == 3:
            return max(lits)
        elif t == 5:
            return int(lits[0] > lits[1])
        elif t == 6:
            return int(lits[0] < lits[1])
        return int(lits[0] == lits[1])
exp = parse(bits)
print("Part 1:", total_v)
print("Part 2:", exp)