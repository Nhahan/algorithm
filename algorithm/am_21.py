N = 4
M = 7
T = [10, 15, 17, 20]
# N = 5
# M = 20
# T = [4, 42, 40, 26, 46]
# import sys
#
# N, M = map(int, sys.stdin.readline().split())
# T = list(map(int, sys.stdin.readline().split()))

def binary(target, numbers):
    num_min = numbers[0]
    num_max = numbers[len(numbers)-1]

    avg = (num_max + num_min) // 2

    while num_min <= num_max:
        sum_T = 0
        for t in T:
            if t - avg > 0:
                sum_T += t - avg
        if target + len(T) > sum_T >= target:
            return avg
        elif sum_T < target:
            num_max = avg - 1
        else:
            num_min = avg + 1
        avg = (num_max + num_min) // 2
    return False

print(binary(M, T))