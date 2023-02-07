n = int(input())
wine = [0]*10001
for i in range(1,n+1):
    wine[i]=int(input())

dp = [0]*10001
dp[1] = wine[1]
dp[2] = wine[1]+wine[2]
dp[3] = max(wine[2]+wine[3], wine[1]+wine[3], wine[1]+wine[2])

for i in range(4, n+1):
    dp[i] = max(dp[i-3]+wine[i-1]+wine[i], dp[i-2]+wine[i], dp[i-1])

print(dp[n])