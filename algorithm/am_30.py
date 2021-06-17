import sys
from collections import deque


def move_left(queue_input1):
    temp = queue_input1[0]
    queue_input1.popleft()
    queue_input1.append(temp)
    print(queue_input1)
    return queue_input1


def move_right(queue_input2):
    temp = queue_input2[-1]
    queue_input2.pop()
    queue_input2.appendleft(temp)
    print(queue_input2)
    return queue_input2


N, M = map(int, sys.stdin.readline().split())
temp_list = list(map(int, sys.stdin.readline().split()))
M_list = list()  # for temp_list

numbers = list()
answer = list()
for i in range(1, N + 1):
    numbers.append(i)
queue_l = deque(numbers)
queue_r = deque(numbers)

for tmp_num in temp_list:
    M_list.append(numbers[tmp_num - 1])


def left_counter(queue_input, target):
    left_queue = queue_input
    left_counts = 0
    # 왼쪽으로
    while 1:
        if left_queue[0] == target:
            left_queue.popleft()
            break
        else:
            left_queue = move_left(left_queue)
            left_counts += 1
    return [left_queue, left_counts]


def right_counter(queue_input, target):
    right_queue = queue_input
    right_counts = 0
    # 오른쪽으로
    while 1:
        if right_queue[0] == target:
            right_queue.popleft()
            break
        else:
            right_queue = move_right(right_queue)
            right_counts += 1
    return [right_queue, right_counts]


for m in M_list:
    rq = right_counter(queue_l, m)
    lq = left_counter(queue_r, m)
    if rq[1] >= lq[1]:  # left의 counts가 적으면 left를 골라
        queue_l = deque(list(lq[0]))
        queue_r = deque(list(lq[0]))
        answer.append(lq[1])
    else:  # right의 counts가 적으면 right를 골라
        queue_l = deque(list(rq[0]))
        queue_r = deque(list(rq[0]))
        answer.append(rq[1])
print(sum(answer))
