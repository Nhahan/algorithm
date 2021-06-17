import sys
from math import gcd

inp = int(sys.stdin.readline())

for i in range(inp):
    a, b = map(int, sys.stdin.readline().split())
    print(int(a * b / gcd(a, b)))