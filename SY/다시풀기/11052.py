n=int(input())
cost=[0]+list(map(int,input().split()))
dp=[0]*(n+1)

for i in range(1,n+1):
	for j in range(i+1):
		dp[i]=max(dp[j]+cost[i-j],dp[i])
print(dp[n])