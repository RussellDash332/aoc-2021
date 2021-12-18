import sys

class SnailNumber(list):
    def __init__(self, val):
        self.parent = None
        super().__init__(val)

def explode(snail_pair):
    pred = snail_pair
    suc = snail_pair
    use_pred = True
    use_suc = True

    while pred is pred.parent[0]:
        pred = pred.parent
        if pred.parent == None:
            use_pred = False
            break
    while suc is suc.parent[1]:
        suc = suc.parent
        if suc.parent == None:
            use_suc = False
            break

    if use_pred:
        if type(pred.parent[0]) != int:
            pred = pred.parent[0]
            while type(pred[1]) != int:
                pred = pred[1]
            pred[1] += snail_pair[0]
        else:
            pred.parent[0] += snail_pair[0]
    if use_suc:
        if type(suc.parent[1]) != int:
            suc = suc.parent[1]
            while type(suc[0]) != int:
                suc = suc[0]
            suc[0] += snail_pair[1]
        else:
            suc.parent[1] += snail_pair[1]

    # Aliasing issue
    if snail_pair.parent[0] is snail_pair:
        snail_pair.parent[0] = 0
    else:
        snail_pair.parent[1] = 0

def split(x, which):
    k = x[which]
    tmp = SnailNumber([k//2, k - k//2])
    tmp.parent = x
    x[which] = tmp

def check_explode(snail, depth):
    if type(snail) != int:
        if check_explode(snail[0], depth + 1):
            return True
        if check_explode(snail[1], depth + 1):
            return True
        if depth > 3:
            explode(snail)
            return True
        return False
    return False

def check_split(snail):
    if type(snail) != int:
        if type(snail[0]) == int and snail[0] > 9:
            split(snail, 0)
            return True
        if check_split(snail[0]):
            return True
        if type(snail[1]) == int and snail[1] > 9:
            split(snail, 1)
            return True
        if check_split(snail[1]):
            return True
        return False
    return False

def make_snail_number(lst):
    if type(lst) == int:
        return lst
    tmp = SnailNumber(list(map(make_snail_number, lst)))
    for i in range(2):
        if type(tmp[i]) != int:
            tmp[i].parent = tmp
    return tmp

snail = make_snail_number(eval(input().strip()))
lists = []
for line in sys.stdin:
    snail = SnailNumber([snail, make_snail_number(eval(line.strip()))])
    lists.append(line.strip())
    snail[0].parent, snail[1].parent = snail, snail
    while True:
        if not check_explode(snail, 0):
            if not check_split(snail):
                break

def magnitude(snail):
    if type(snail) == int:
        return snail
    return 3 * magnitude(snail[0]) + 2* magnitude(snail[1])
print("Part 1:", magnitude(snail))

addtwo = []
for i in lists:
    for j in lists:
        if i != j:
            snail = SnailNumber([make_snail_number(eval(i)), make_snail_number(eval(j))])
            snail[0].parent, snail[1].parent = snail, snail
            while True:
                if not check_explode(snail, 0):
                    if not check_split(snail):
                        break
            addtwo.append(snail)
print("Part 2:", max(map(magnitude, addtwo)))