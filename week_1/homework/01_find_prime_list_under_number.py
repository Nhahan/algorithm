input = 20


def find_prime_list_under_number(number):
    prime_number = []
    discriminant = 0
    for num in range(2, number + 1):
        for i in range(1, num + 1):
            if num % i == 0:
                discriminant += 1
        if discriminant == 2:
            prime_number.append(num)
        discriminant = 0
    return prime_number


result = find_prime_list_under_number(input)
print(result)