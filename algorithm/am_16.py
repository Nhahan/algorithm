a, b = map(int, input().split())
su_a = 2
so_a = []
while su_a <= a:
    if a % su_a == 0:
        so_a.append(su_a)
        a = a // su_a
    else:
        su_a += 1
su_b = 2
so_b = []
while su_b <= b:
    if b % su_b == 0:
        so_b.append(su_b)
        b = b // su_b
    else:
        su_b += 1
answer_list = list()
while_list_a = so_a
answer_min = 1
for a in while_list_a:
    if a in so_b:
        answer_list.append(a)
        so_a.remove(a)
        so_b.remove(a)
for an in answer_list:
    answer_min = answer_min * an
print(answer_min)
answer_list = answer_list + so_a + so_b
answer_max = 1
for an in answer_list:
    answer_max = answer_max * an
print(answer_max)