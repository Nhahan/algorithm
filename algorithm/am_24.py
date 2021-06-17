import sys

inp = int(sys.stdin.readline())

stack = list()
for i in range(inp):
    a = sys.stdin.readline()
    yes_or_no = 0
    if a.count("(") == a.count(")"):
        for j in a:
            if j == "(":
                stack.append("(")
            else:
                if j == ")" and "(" not in stack:
                    print("NO")
                    break
                elif "(" in stack:
                    stack.pop()
            yes_or_no += 1
        if yes_or_no == len(a):
            print("YES")
    else:
        print("NO")