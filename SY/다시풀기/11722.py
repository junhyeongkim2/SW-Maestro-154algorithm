n=int(input())
li=list(map(int,input().split()))
dp=[0]*n
dp[0]=1

for i in range(1,n):
	for j in range(i):
		#i번째 이전 숫자의 최대 dp값 가져오기
		if li[j]>li[i]:
			dp[i]=max(dp[i],dp[j])
	#i번째 숫자 dp 횟수 포함
	dp[i]+=1
print(max(dp))