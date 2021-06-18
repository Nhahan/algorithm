import sys
from collections import Counter

N = int(sys.stdin.readline())

nums = []
for n in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)
print(int(round((sum(nums) / N), 0)))  # 1
nums.sort()
answer4 = max(nums) - min(nums)
print(nums[N // 2])  # 2

if len(nums) == 1:  # 3
    print(nums[0])
else:
    counter = Counter(nums)
    tuple_list = counter.most_common()
    if tuple_list[0][1] == tuple_list[1][1]:
        print(tuple_list[1][0])
    else:
        print(tuple_list[0][0])

print(answer4)  # 4
