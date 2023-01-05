# 11726번 2xn 타일링
# https://www.acmicpc.net/problem/11726

N = int(input())
dp = [0, 1, 2]
for i in range(3, N+1):
    dp.append(dp[i-1]+dp[i-2])
print(dp[N]%10007)