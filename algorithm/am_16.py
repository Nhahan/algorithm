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
while_list_b = so_b
answer_min = 1
for i in range(len(while_list_a)):
    if while_list_a[i] in so_b:
        ai = while_list_a[i]
        so_b.remove(while_list_a[i])
        answer_list.append(ai)
for an in answer_list:
    answer_min = answer_min * an
print(answer_min)
max_answer_list = so_a + so_b
answer_max = 1
for an in max_answer_list:
    answer_max = answer_max * an
print(answer_max)
