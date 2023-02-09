dp = [[1]*201 for _ in range(201)]

n, k = map(int, input().split())

for i in range(1, n+1):
    for k in range(2, k+1):
        dp[i][k] = (dp[i-1][k]+dp[i][k-1])%int(1e9)

print(dp[i][k])