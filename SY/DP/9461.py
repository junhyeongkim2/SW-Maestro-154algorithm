t=int(input())
li=[int(input()) for _ in range(t)]
dp=[0]*(max(li))
dp[0]=1
dp[1]=1
dp[2]=1
dp[3]=2
dp[4]=2

for i in range(5,max(li)):
	dp[i]=dp[i-1]+dp[i-5]
for i in li:
	print(dp[i-1])
