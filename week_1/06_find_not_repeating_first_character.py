input = "abacabade"
input2 = "abadabac"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    array = [0] * 26
    for i in range(len(string)):
        array[ord(string[i]) - 97] += 1
    min_num = 1
    print(array)
    for i in range(len(array)):
        if i == 0:
            pass
        elif array[i] != 0 and array[i-1] != 0:
            if array[i] < array[i-1]:
                min_num = array[i]
            else:
                min_num = array[i-1]
    for i in range(len(string)):
        if array[ord(string[i]) - ord("a")] == min_num:
            return string[i]


result = find_not_repeating_character(input)
print(result)

result = find_not_repeating_character(input2)
print(result)
