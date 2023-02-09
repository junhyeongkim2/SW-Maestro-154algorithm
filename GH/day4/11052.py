n = int(input())
data = list(map(int, input().split()))
data.insert(0,0)
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i-j]+data[j], dp[i])

print(dp[n])