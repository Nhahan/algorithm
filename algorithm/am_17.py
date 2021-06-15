c = int(input())

for ci in range(c):
    H, W, N = map(int, input().split())

    floor = H if N % H == 0 else N % H
    room = N // H + 1 if N % H != 0 else N // H

    print(floor * 100 + room)
