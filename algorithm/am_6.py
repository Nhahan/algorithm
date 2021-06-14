nums = list()
ans = list()
for i in range(1, 10001):
    ans.append(i)
    n1 = int(str(i)[-1])
    try:
        n2 = int(str(i)[-2])
    except IndexError:
        n2 = 0
    try:
        n3 = int(str(i)[-3])
    except IndexError:
        n3 = 0
    try:
        n4 = int(str(i)[-4])
    except IndexError:
        n4 = 0
    try:
        n5 = int(str(i)[-5])
    except IndexError:
        n5 = 0
    n = i + n1 + n2 + n3 + n4 + n5
    if n not in nums and n <= 10000:
        nums.append(n)
self_num = list()
for an in ans:
    if an not in nums:
        self_num.append(an)
self_num.sort()
for self in self_num:
    print(self)
