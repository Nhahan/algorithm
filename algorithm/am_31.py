import sys
from collections import deque

inp = int(sys.stdin.readline())
stack = list()
stack = deque(stack)
for i in range(inp):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        stack.appendleft(a[1])
    elif a[0] == "back":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[0])
    elif a[0] == "size":
        print(len(stack))
    elif a[0] == "empty":
        if len(stack) == 0:
            print("1")
        else:
            print("0")
    elif a[0] == "pop":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif a[0] == "front":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])