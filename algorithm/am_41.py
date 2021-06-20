import sys

N = int(sys.stdin.readline())

memo = {
    1: 1,
    2: 1
}
def fibo(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo(n - 1, fibo_memo) + fibo(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo
    return nth_fibo


for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        print("1 0")
    elif num == 1:
        print("0 1")
    elif num == 2:
        print("1 1")
    else:
        print(fibo(num - 1, memo), fibo(num, memo))