world = [0] * 10
nums = list(map(int, input().split(",")))
for i in nums:
    world[i] += 1
for k in range(256):
    new = [0] * 10
    for i in range(10):
        if i:
            new[i - 1] += world[i]
        else:
            new[6] += world[0]
            new[8] += world[0]
    world = new
    if k == 79:
        print("Part 1:", sum(world))
print("Part 2:", sum(world))

"""
Codegolf-ish version thanks to @xsot

a=map(eval(input()).count,range(9))
exec("x,*a=a;a+=x,;a[6]+=x;"*80)
print(sum(a))
exec("x,*a=a;a+=x,;a[6]+=x;"*176)
print(sum(a))
"""