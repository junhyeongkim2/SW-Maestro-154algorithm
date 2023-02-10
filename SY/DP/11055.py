n=int(input())
li=list(map(int,input().split()))
dp=[0]*n
dp=li[:]

for i in range(n):
	for j in range(i):
		if li[j]<li[i] and dp[i]<dp[j]+li[i]:
			dp[i]=dp[j]+li[i]
print(max(dp))