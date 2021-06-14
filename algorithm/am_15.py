aliquot = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[0] ** 2) if aliquot == 1 else print(a[0] * a[-1])