input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    answer = [0] * 2
    when1 = [0] * len(string)
    when2 = [0] * len(string)

    for i in range(len(string)):
        if i == 0 and string[i] == "1":
            answer[0] += 1
            when1[i] += 1
        elif string[i] == "1":
            if when1[i - 1] == 1:
                when1[i] += 1
            else:
                answer[0] += 1
                when1[i] += 1

    for i in range(len(string)):
        if i == 0 and string[i] == "0":
            answer[1] += 1
            when2[i] += 1
        elif string[i] == "0":
            if when2[i - 1] == 1:
                when2[i] += 1
            else:
                answer[1] += 1
                when2[i] += 1

    return min(answer)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 000000
# 000001
# 000010
# 000011
# 000100
# 000101
# 000110
# 000111
# 001000
# 001001
# 001010
# 001011
# 001100
# 001101
# 001110
# 001111
# 010000
# 010001
# 010010
# 010011
# 010100
# 010101
# 010111
# 011000
# 011001
# 011010
# 011011
# 011100
# 011101
# 011110
# 011111
# 100000
# 100001
# 100010
# 100011
# 100100
# 100101
# 100110
# 100111
# 101000
# 101001
# 101010
# 101011
# 101100
# 101101
# 101110
# 101111
# 110000
# 110001
# 110010
# 110011
# 110100
# 110101
# 110110
# 110111
# 111000
# 111001
# 111010
# 111011
# 111100
# 111101
# 111110
# 111111
