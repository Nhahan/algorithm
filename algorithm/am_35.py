import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
nums = list()
for n in range(1, N + 1):
    nums.append(n)
c = list((combinations(nums, M)))
for li in c:
    for l in li:
        print(l) if l == li[-1] else print(l, end=" ")
