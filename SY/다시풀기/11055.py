n=int(input())
li=list(map(int,input().split()))
dp=[0]*n
dp[0]=li[0]

for i in range(1,n):
	for j in range(i):
		if li[j]<li[i]:
			#i번째 이전 최대 dp값 가져오기
			dp[i]=max(dp[i],dp[j])
	#i번째 수 dp값에 더하기
	dp[i]+=li[i]

print(max(dp))