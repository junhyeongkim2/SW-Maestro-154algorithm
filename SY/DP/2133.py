"""
	2 -> 3
	4 -> dp[2] *dp[2] +2 = 11
	6 -> dp[4] *dp[2] + dp[2] *2 +1 =41
	8 -> dp[6] *dp[2] + dp[4] *2 + dp[2] *2 + 2
	점화식 -> dp[n-2]*dp[2] + (dp[2]+dp[4]+ ... + dp[n-2])*2 +2
"""
n=int(input())
if n==1:
	print(0)
else:
	dp=[0]*(n+1)
	dp[2]=3
	for i in range(4,n+1,2):
		dp[i]=3*dp[i-2]+sum(dp[:i-2])*2+2
	print(dp[n])
