# 2133번 타일 채우기
# https://www.acmicpc.net/problem/2133

N = int(input())

dp = [0, 1, 3]
for i in range(3, N+1):
    if i%2==0: dp.append(2*dp[i-1]+dp[i-2])
    else: dp.append(dp[i-1]+dp[i-2])

if N%2==0: print(dp[N])
else: print(0)