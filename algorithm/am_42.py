import sys

N = list(map(str, sys.stdin.readline().split("-")))
N_list = list()
for n in N:
    N_list.append(n.replace("\n", ""))
answer = 0
for i in range(len(N_list)):
    temp = list()
    if i == 0:
        sum_tmp = 0
        tmp = N_list[i].split("+")
        for t in tmp:
            sum_tmp += int(t)
        answer += sum_tmp
    else:
        sum_tmp = 0
        tmp = N_list[i].split("+")
        for t in tmp:
            sum_tmp += int(t)
        answer -= sum_tmp
print(answer)