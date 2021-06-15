import math
a, b = map(int, input().split())
n = b + 1
is_primes = [True] * n
max_length = math.ceil(math.sqrt(n))
for i in range(2, max_length):
    if is_primes[i]:  # if True
        for j in range(2 * i, n, i):
            is_primes[j] = False
prime_number = [i for i in range(a, n) if is_primes[i]]
for num in prime_number:
    if num == 1:
        pass
    else:
        print(num)