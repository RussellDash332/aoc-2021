nums = sorted(map(int, input().split(",")))

# Part 1
median = nums[len(nums) // 2]
print("Part 1:", sum(map(lambda x: abs(x - median), nums)))

# Part 2
def ase(i):
    return sum(map(lambda x: (abs(x - i) * (abs(x - i) + 1)) // 2, nums))
print("Part 2:", ase(sum(nums) // len(nums)))