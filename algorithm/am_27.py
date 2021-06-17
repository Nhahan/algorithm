import sys
from math import comb

inp = int(sys.stdin.readline())

for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    answer = comb(b, a)
    print(answer)