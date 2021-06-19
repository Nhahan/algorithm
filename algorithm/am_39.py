import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
c = list(combinations(a, 3))
temp_sum = M
answer = list()
for a in c:
    if 0 <= M - sum(a) <= temp_sum:
        temp_sum = M - sum(a)
        answer = a
print(sum(answer))
