import sys

inp = int(sys.stdin.readline())

stack = list()
for i in range(inp):
    a = int(sys.stdin.readline())
    if a == 0:
        if len(stack) != 0:
            stack.pop()
    else:
        stack.append(a)
print(sum(stack))