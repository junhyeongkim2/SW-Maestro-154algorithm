# 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579

import sys
read = sys.stdin.readline

N = int(read().strip())
stair = [int(read().strip()) for _ in range(N)]
dp = [0] * N

if N==1:
    print(stair[0])
    exit()
elif N==2:
    print(stair[0] + stair[1])
    exit()
dp[0] = stair[0]
dp[1] = stair[0] + stair[1]
dp[2] = max(dp[0], stair[1]) + stair[2]
for i in range(3, N):
    dp[i] = max(dp[i-3]+stair[i-1], dp[i-2]) + stair[i]
print(dp[N-1])