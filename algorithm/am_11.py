import math
C = int(input())
for cal in range(C):
    x, y = list(map(int, input().split()))
    distance = y - x
    n = math.floor(math.sqrt(abs(distance)))
    if distance == n ** 2:
        print(2 * n - 1)
    elif n ** 2 < distance <= n ** 2 + n:
        print(2 * n)
    else:
        print(2 * n + 1)