a, b, v = map(int, input().split())
i = (v - b) / (a - b)
print(int(i) if i == int(i) else int(i)+1)