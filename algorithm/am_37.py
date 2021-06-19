import sys

N = int(sys.stdin.readline())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    r_d = max(r2, r1) - min(r2, r1)
    r_s = r1 + r2
    if r_d < distance < r_s:
        print(2)
    elif (x1, y1, r1) == (x2, y2, r2):
        print(-1)
    elif r_d == distance or r_s == distance:
        print(1)
    elif r_s < distance or distance < r_d or distance == 0:
        print(0)
