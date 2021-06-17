import sys
from math import factorial

a, b = map(int, sys.stdin.readline().split())

answer = factorial(a) / factorial(b) / factorial(a - b)

print(int(answer))