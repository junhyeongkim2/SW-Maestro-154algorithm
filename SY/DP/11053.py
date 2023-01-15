n=int(input())
a=list(map(int, input().split()))
dp=[0]*n
dp[0]=1
for i in range(1,n):
	for j in range(i):
		if a[i]>a[j]:
			"""
			dp[i]와 dp[j]를 비교하는 이유(17번째 줄)
			a[j]가 a[i]보다 작더라도 j번째 전에 비교했던 수보다 크다는 보장이 없음
			그래서 dp[j]와 dp[i]를 비교하여
			 -> dp[i]>dp[j]라면
			 	j번째 수까지 a[i]보다 작은 수는 dp[j]개 이므로 dp[i]=dp[j]로 업데이트
			 -> dp[i]<dp[j]라면
			 	가장 긴 수열을 찾아야 하기 때문에 해당 사항 없음
			"""
			dp[i]=max(dp[j],dp[i])
	dp[i]+=1
print(max(dp))
