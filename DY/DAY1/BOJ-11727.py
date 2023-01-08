# 11727번 2xn 타일링 2
# https://www.acmicpc.net/problem/11727

N = int(input())
dp = [0, 1, 3]
for i in range(3,N+1):
    dp.append(dp[i-1]+dp[i-2]*2)
print(dp[N]%10007)