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
    left_up = logic(x, y, n // 2)
    right_up = logic(x + n // 2, y, n // 2)
    left_down = logic(x, y + n // 2, n // 2)
    right_down = logic(x + n // 2, y + n // 2, n // 2)
    white = left_up[0] + right_up[0] + left_down[0] + right_down[0]
    blue = left_up[1] + right_up[1] + left_down[1] + right_down[1]
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
