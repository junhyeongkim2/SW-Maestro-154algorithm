#참고 해결
n=int(input())
li=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=li[0]

if n>1:
	dp[1]=dp[0]+li[1]
if n>2:
	dp[2]=max(dp[1], li[0]+li[2], li[1]+li[2])

for i in range(3,n):
	s1=dp[i-1] #현재거 재외
	s2=dp[i-2]+li[i] #이전거 제외
	s3=dp[i-3]+li[i-1]+li[i] #이전 이전거 제외

	dp[i]=max(s1,s2,s3)

print(max(dp))