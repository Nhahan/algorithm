C = int(input())

for cal in range(C):
    a = list(map(int, input().split()))
    avg = sum(a[1:]) / a[0]
    N = 0
    for i in range(1, len(a)):
        if a[i] > avg:
            N += 1
    percentage = (N / a[0]) * 100
    print(f"{percentage:.3f}%")