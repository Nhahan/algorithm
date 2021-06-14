n = int(input()) - 1
nums = list()
i = 0
for i in range(3000000):
    if "666" in str(i):
        nums.append(i)
        i += 1
nums.sort()
print(nums[n])
