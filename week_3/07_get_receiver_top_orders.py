top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(top_heights):
    n = len(top_heights)
    answer = [0] * n
    for i in range(n):
        for j in range(n):
            if j > i:
                continue
            if top_heights[i] < top_heights[i - j] and j < i:
                answer[i] = i - j + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!