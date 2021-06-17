finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_exist_target_number_binary(target, numbers):
    arr = sorted(numbers)
    num_min = arr[0]
    num_max = arr[len(arr)-1]

    avg = (num_max + num_min) // 2

    while num_min <= num_max:
        if target == avg:
            return True
        elif target < avg:
            num_max = avg - 1
        else:
            num_min = avg + 1
        avg = (num_max + num_min) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)