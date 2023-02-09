n = int(input())
dp = [0]*301
data = []
for i in range(n):
    data.append(int(input()))

dp[0] = data[0]
if n>=2:
    dp[1] = data[0]+data[1]
if n>=3:
    dp[2] = max(data[1]+data[2], data[0]+data[2])
    for i in range(3, n):
        dp[i] = max(dp[i-3]+data[i-1]+data[i], data[i] + dp[i-2])

print(dp[n-1])