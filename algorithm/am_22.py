# 14
# push 1
# push 2
# top
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# top
import sys

inp = int(sys.stdin.readline())
stack = list()
for i in range(inp):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        stack.append(a[1])
    elif a[0] == "top":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
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