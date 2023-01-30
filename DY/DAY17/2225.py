# 2225번 합분해
# https://www.acmicpc.net/problem/2225

N, K = map(int, input().split())
dp = [[1]*(K+1)] + [[0]*(K+1) for _ in range(N)]
for num in range(1, N+1):
    for space in range(1, K+1):
        if space == 1: dp[num][space] = 1
        else:
            for prev in range(num+1):
                dp[num][space] += dp[prev][space-1]
                dp[num][space] %= 1000000000
print(dp[N][K])