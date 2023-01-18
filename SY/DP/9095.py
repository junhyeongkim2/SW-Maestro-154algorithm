n=int(input())
t=[]
for i in range(n):
	io=int(input())
	t.append(io)
dp=[0]*(max(t)+1)
dp[1]=1
dp[2]=2
dp[3]=4

for i in range(4,max(t)+1):
	dp[i]=dp[i-2]+dp[i-1]+dp[i-3]

for tc in t:
	print(dp[tc])