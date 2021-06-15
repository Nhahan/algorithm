

N = int(input())
answer = list()
def logic(n, start, end):
    mid = 6 - start - end
    if n == 1:
        logic(n - 1, 1, 3)
        answer.append([start, end])
    if n > 1:
        logic(n - 1, start, mid)
        answer.append([start, end])
        logic(n - 1, mid, end)
logic(N, 1, 3)
print(len(answer))
for print_answer in answer:
    print(print_answer[0], print_answer[1])


