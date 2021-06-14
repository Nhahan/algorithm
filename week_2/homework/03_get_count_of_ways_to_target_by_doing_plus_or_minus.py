import random

numbers = [2, 1, 6, 3, 3]
target_number = 3

def get_count_of_ways_to_target_by_doing_plus_or_minus(array, target):
    # 구현해보세요!
    pm = [1, -1]
    cases = []
    while 1:
        ran_num = []
        for arr in array:
            ran_num.append(arr * random.choice(pm))
        cases.append(ran_num)
        cases = list(set([tuple(case) for case in cases]))
        print(cases)
        if len(cases) == (2 ** len(array)):
            break
    answer = []
    for case in cases:
        answer.append(sum(case))
    return answer.count(target)

print(get_count_of_ways_to_target_by_doing_plus_or_minus(numbers, target_number))  # 5를 반환해야 합니다!