# 2193번 이친수
# https://www.acmicpc.net/problem/2193

N = int(input())
dp = [0, 1]
for i in range(2, N+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[N])