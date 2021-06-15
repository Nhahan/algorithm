# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3
# inp = int(input())
# array = list()
# for i in range(inp):
#     a, b = map(int, input().split())
#     array.append([a, b])
# n = len(array)
# for i in range(1, n):
#     for j in range(i):
#         if array[i - j - 1][1] > array[i - j][1]:
#             array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
#         elif array[i - j - 1][1] == array[i - j][1] and array[i - j - 1][0] > array[i - j][0]:
#             array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
#         else:
#             break
# for arr in array:
#     print(arr[0], arr[1])


# 퀵 정렬.. x좌표 때문에 실패
# inp = int(input())
# array = list()
# for i in range(inp):
#     a, b = map(int, input().split())
#     array.append([a, b])
# print(array)
# def quick(arr):
#     if len(arr) <= 1:
#         return arr
#     else:
#         pivot = arr[0][1]
#         less = [number for number in arr[1:] if number[1] <= pivot]
#         greater = [number for number in arr[1:] if number[1] > pivot]
#         return quick(less) + [arr[0]] + quick(greater)
#
# result = quick(array)
# print(result)

inp = int(input())
array = list()
y_list = list()
for i in range(inp):
    a, b = map(int, input().split())
    array.append([a, b])
    if b not in y_list:
        y_list.append(b)
y_list.sort()
array.sort(key=lambda x: x[1])
array_dict = {}
for arr in array:
    if arr[1] not in array_dict:
        array_dict[arr[1]] = 1
    elif arr[1] in array_dict:
        array_dict[arr[1]] += 1
answer = list()
for y in range(len(y_list)):
    temp = list()
    if array_dict[y_list[y]] == 1:
        answer.append(array[0])
        array.remove(array[0])
    else:
        for i in range(array_dict[y_list[y]]):
            temp.append(array[0])
            array.remove(array[0])
        temp.sort(key=lambda x: x[0])
        answer += temp
for ans in answer:
    print(ans[0], ans[1])