n=int(input())
p=list(map(int,input().split()))
p.insert(0,0)
dp=[0]*(n+1) #dp[i]는 카드의 개수 i개를 만들 때 지불할 최대금액을 저장

for i in range(1,n+1):
	for j in range(i+1):
		"""
		i가 4일 때 경우의 수
		- dp[0]+p[4]
		- dp[1]+p[3]
		- dp[2]+p[2]
		- dp[3]+p[1]
		이 때, dp[0]~dp[3]은 인덱스 개 만큼 카드팩을 살 때의 최대금액이 저장됨
		"""
		dp[i]=max(dp[i],dp[j]+p[i-j])

print(dp[n])