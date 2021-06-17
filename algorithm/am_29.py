import sys

def push():
    stack_list.append(numbers.pop())
    plus_minus_list.append("+")

def pop():
    answer_list.append(stack_list.pop())
    num_list.remove(num_list[0])
    plus_minus_list.append("-")

inp = int(sys.stdin.readline())
numbers = list()  # 8 7 6 5 4 3 2 1
num_list = list()  # 4 3 6 8 7 5 2 1
stack_list = list()
answer_list = list()
plus_minus_list = list()
for i in range(inp, 0, -1):
    numbers.append(i)
for i in range(inp):
    a = int(sys.stdin.readline())
    num_list.append(a)
n = 0
while n < inp * 2 + 1:
    if len(stack_list) > 0:
        if stack_list[-1] == num_list[0]:
            pop()
        elif len(numbers) > 0:
            push()
    elif len(stack_list) == 0 and len(numbers) > 0:
        push()
    elif len(numbers) > 0:
        push()
    else:
        for pm in plus_minus_list:
            print(pm)
        break
    n += 1
    if n == inp * 2 + 1:
        print("NO")
        break