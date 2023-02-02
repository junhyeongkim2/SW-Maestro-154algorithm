n = int(input())

dp = [0] * 1001 # 1001이 아닌 (n+1)을 곱하면 런타임 에러가 나온다. 이유는 모름

dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
  dp[i] = dp[i-1] + dp[i-2]

print(dp[n]%10007)

