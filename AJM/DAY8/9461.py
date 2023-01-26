#9461 파도반 수열

x = int(input())

for k in range(x):
    n = int(input())

    dp=[0]*(101)

    dp[1]=1
    dp[2]=1
    dp[3]=1

    for i in range (4,n+1):
        dp[i] = dp[i-3]+dp[i-2]
    print(dp[n])
