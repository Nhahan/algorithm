# C = int(input())
# answer = C
# for time in range(C):
#     a = input()
#     for i in range(len(a)):
#         for j in range(2, len(a)):
#             try:
#                 a = a.replace(a[i] * j, a[i])
#             except IndexError:
#                 pass
#     for i in range(len(a)):
#         temp = a[0]
#         a = a.replace(temp, "", 1)
#         if temp in a:
#             answer -= 1
#             break
# print(answer)
#
#
# C = int(input())
# answer = 0
# for time in range(C):
#     a = input()
#     a_list = list()
#     for char in a:
#         a_list.append(char)
#     a_set = list(set(a_list))
#     for i in range(len(a_set)):
#         exist_idx = int(a.find(a_set[i])) + 1
#         for j in range(1, len(a) - 1):
#             try:
#                 if a[exist_idx] == a_set[i]:
#                     a = a.replace(a_set[i], "", 1)
#                 else:
#                     break
#             except IndexError:
#                 pass
#     counts = list()
#     for letter in a_set:
#         counts.append(a.count(letter))
#     if counts.count(1) == len(a_set):
#         answer += 1
# print(answer)

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