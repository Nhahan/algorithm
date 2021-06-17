C = int(input())
answer = 0
for time in range(C):
    inputs = input()
    char_check_list = list()
    checker = 0
    for i in range(len(inputs)):
        if inputs[i] not in char_check_list:
            char_check_list.append(inputs[i])
        else:
            if inputs[i-1] == inputs[i]:
                pass
            else:
                checker += 1
    if checker == 0:
        answer += 1
print(answer)