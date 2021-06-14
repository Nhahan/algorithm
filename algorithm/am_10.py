kg = int(input())
chance = list()
for a in range(kg // 5 + 1):
    for b in range(kg // 3 + 1):
        if a * 5 + b * 3 == kg:
            chance.append(a + b)
print(-1) if len(chance) == 0 else print(min(chance))