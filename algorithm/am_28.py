while 1:
    stack = list()
    a = input()
    if a == ".":
        break
    else:
        if a.count("(") == a.count(")") and a.count("[") == a.count("]"):
            for j in range(len(a)):
                if a[j] == "(":
                    stack.append("(")
                elif a[j] == "[":
                    stack.append("[")
                elif a[j] == ")":
                    if "(" in stack:
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            print("no")
                            break
                    else:
                        print("no")
                        break
                elif a[j] == "]":
                    if "[" in stack:
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            print("no")
                            break
                    else:
                        print("no")
                        break
                if j == (len(a) - 1):
                    print("yes")
        else:
            print("no")