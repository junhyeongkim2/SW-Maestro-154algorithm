# 9465번 스티커
# https://www.acmicpc.net/problem/9465

import sys
read = sys.stdin.readline

T = int(read().strip())
for _ in range(T):
    N = int(read().strip())
    sticker = [[0]+list(map(int, read().split())) for _ in range(2)]
    dp = [[0]*(N+1) for _ in range(2)]

    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]
    for c in range(2, N+1):
        for r in range(2):
            dp[r][c] = max(dp[r-1][c-1], dp[r-1][c-2]) + sticker[r][c]
    print(max(dp[0][N], dp[1][N]))