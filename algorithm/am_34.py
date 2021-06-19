import sys

N = int(sys.stdin.readline())
papers = list()

for i in range(N):
    append_list = list(map(int, sys.stdin.readline().split()))
    papers.append(append_list)


def logic(x, y, n):
    if n == 1:
        if papers[x][y] == 1:
            return [0, 1]  # white, blue
        else:
            return [1, 0]  # white, blue
    answer = [0, 0]  # white, blue
    next_n = n // 2
    left_upside = logic(x, y, next_n)
    right_upside = logic(x + next_n, y, next_n)
    left_downside = logic(x, y + next_n, next_n)
    right_downside = logic(x + next_n, y + next_n, next_n)
    white = left_upside[0] + right_upside[0] + left_downside[0] + right_downside[0]
    blue = left_upside[1] + right_upside[1] + left_downside[1] + right_downside[1]

    if white == 4 and blue == 0:
        answer[0] = 1
        answer[1] = 0
    elif white == 0 and blue == 4:
        answer[0] = 0
        answer[1] = 1
    else:
        answer[0] += white
        answer[1] += blue
    return answer


white_blue = logic(0, 0, int(N))
print(white_blue[0])
print(white_blue[1])
