input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    answer = 0
    for i in input:
        plus = answer + i
        mult = answer * i
        if plus > mult:
            answer = plus
        else:
            answer = mult
    return answer


result = find_max_plus_or_multiply(input)
print(result)