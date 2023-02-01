n=int(input())
dp=[[0]*10 for _ in range(n+1)]

for i in range(10):
	dp[1][i]=1

for i in range(2,n+1):
	dp[i][0]=1
	for j in range(1,10):
		for z in range(0,j+1):
			dp[i][j]+=dp[i-1][z]

print(sum(dp[n])%10007)