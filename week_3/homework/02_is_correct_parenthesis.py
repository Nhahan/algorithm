s = "(())()"


def is_correct_parenthesis(string):
    lists = []
    for i in range(len(string)):
        if string[i] == "(":
            lists.append([string[i]])
        elif string[i] == ")":
            for m in range(len(lists)):
                if lists[m][0] == "(" and len(lists[m]) == 1:
                    lists[m].append(string[i])
                    break
                else:
                    continue
                    if m == len(lists) - 1:
                        return False
    for j in range(len(lists)):
        if lists[j][0] == ")":
            return False
        if len(lists[j]) <= 1:
            return False
    return True


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
print(is_correct_parenthesis("(((("))  # F
print(is_correct_parenthesis("((())))("))  # F
print(is_correct_parenthesis(")((((("))  # F
print(is_correct_parenthesis(")()((((("))  # F
print(is_correct_parenthesis(")()((((()))"))  # F
print(is_correct_parenthesis("))(())(()()("))  # F
print(is_correct_parenthesis("(()))(()"))  # F
print(is_correct_parenthesis("(()))(()"))  # F
print(is_correct_parenthesis("()()()()()()()()((()))(())(())()"))  # T
