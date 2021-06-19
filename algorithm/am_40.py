import sys

N = int(sys.stdin.readline())
if 3 / 4 * N < 1:
    l_N = int(3 / 4 * N)
else:
    l_N = 1
answer = list()
for i in range(l_N, int(3 / 2 * N)):
    g = int(str(i)[-1])
    f = int(str(i)[-2]) if i >= 10 else 0
    e = int(str(i)[-3]) if i >= 100 else 0
    d = int(str(i)[-4]) if i >= 1000 else 0
    c = int(str(i)[-5]) if i >= 10000 else 0
    b = int(str(i)[-6]) if i >= 100000 else 0
    a = int(str(i)[-7]) if i >= 1000000 else 0
    if i + a + b + c + d + e + f + g == N:
        answer.append(i)
print(0) if len(answer) == 0 else print(min(answer))

