# 1699번 제곱수의 합
# https://www.acmicpc.net/problem/1699

import math

N = int(input())
dp = [0]+[1]*(N)
for n in range(1, N+1):
    if n**(1/2)%1==0: # 제곱수가 나머지가 없는 경우(정수인 경우)
        dp[n] = 1
        continue
    dp[n] = dp[n-1]+1
    for i in range(1, math.floor(n**(1/2))+1):
        dp[n] = min(dp[n-i**2]+1, dp[n])
print(dp[N])