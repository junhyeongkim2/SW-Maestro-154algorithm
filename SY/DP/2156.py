n=int(input())
w=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=w[0]

if n>1:
	dp[1]=w[0]+w[1]

if n>2:
	dp[2]=max(dp[1],w[1]+w[2],w[0]+w[2])

for i in range(3,n):
	c1=w[i]+w[i-1]+dp[i-3] #현재, 이전 포도주 마시고 전전 포도주 안마신 경우
	c2=w[i]+dp[i-2] #현재, 전전 포도주 마시고 이전 포도주 안마신 경우
	c3=dp[i-1] #이전, 전전 포도주 마시고 현재 포도주 안마신 경우
	dp[i]=max(c1,max(c2,c3))

print(max(dp))