import sys
from collections import deque


def move_and_pop():
    for _ in range(K - 1):
        temp = num_list.popleft()
        num_list.append(temp)


N, K = map(int, sys.stdin.readline().split())
num_list = deque()
answer = list()
for i in range(1, N + 1):
    num_list.append(i)
for _ in range(N):
    move_and_pop()
    answer.append(num_list.popleft())
print("<", end="")
for ans in answer:
    if ans == answer[-1]:
        print(str(ans) + ">", end="")
    else:
        print(str(ans) + ", ", end="")
