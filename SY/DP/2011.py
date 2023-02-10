n=list(map(int,input()))
dp=[0]*(len(n)+1)
if n[0]==0:
	print(0)
else:
	n.insert(0,0)
	dp[0]=dp[1]=1
	for i in range(2,len(n)):
		if n[i]>0:
			dp[i]+=dp[i-1]
		if 10<=n[i-1]*10+n[i]<27: #00은 제외, 10부터 가능
			dp[i]+=dp[i-2]
	print(dp[-1]%1000000)