N = int(input())
stair = [int(input()) for _ in range(N)]
dp = list()
dp.append(stair[0])
if len(stair) == 1:
    print(dp[-1])
elif len(stair) == 2:
    print(dp[-1] + stair[-1])
else:
    dp.append(dp[0] + stair[1])
    dp.append(max(dp[0] + stair[2], stair[1] + stair[2]))

    for i in range(3, N):
        dp.append(max(stair[i] + stair[i - 1] + dp[i - 3], stair[i] + dp[i - 2]))
    print(dp[-1])