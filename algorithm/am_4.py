init = int(input())

a = init // 10
b = init % 10
N = 0

def loop(a1, b1, answer):
    aa = a1 + b1
    new_num = b1 * 10 + aa % 10
    answer += 1
    if new_num == init:
        return print(answer)
    a2 = new_num // 10
    b2 = new_num % 10
    return loop(a2, b2, answer)

loop(a, b, N)