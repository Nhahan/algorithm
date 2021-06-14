input_string = input()
lower_string = input_string.lower()
arr = [0] * 26
for char in lower_string:
    a = ord(char) - ord("a")
    arr[a] += 1
answer = list()
for idx in range(len(arr)):
    if max(arr) == arr[idx]:
        answer.append(idx)
if len(answer) > 1:
    print("?")
else:
    print((chr(answer[0] + ord("a"))).upper())