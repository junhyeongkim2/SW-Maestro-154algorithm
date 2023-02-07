dp = [0]*100

n = int(input())
dp[1] = 1
dp[2] = 1

for i in range(3,n+1):
    dp[i] = dp[i-1]+dp[i-2]

print(dp[n])