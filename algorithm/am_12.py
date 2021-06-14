import math

n = 123456 * 2 + 1
is_primes = [True] * n
max_length = math.ceil(math.sqrt(n))
for i in range(2, max_length):
    if is_primes[i]:  # if True
        for j in range(2 * i, n, i):
            is_primes[j] = False
prime_number = [i for i in range(2, n) if is_primes[i]]
while 1:
    nums = int(input())
    if nums == 0:
        break
    else:
        counts = 0
        for i in prime_number:
            if nums < i <= 2 * nums:
                counts += 1
        print(counts)
