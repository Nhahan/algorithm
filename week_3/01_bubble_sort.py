input = [4, 6, 2, 9, 1]


def bubble_sort(array):
    num_list = array
    for num in range(len(num_list) - 1):
        for i in range(len(num_list) - 1 - num):
            if num_list[i] > num_list[i + 1]:
                a = num_list[i]
                b = num_list[i + 1]
                num_list[i] = b
                num_list[i + 1] = a
    return num_list


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!