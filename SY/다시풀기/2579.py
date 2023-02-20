n=int(input())
li=[int(input()) for _ in range(n)]
dp=[0]*n
dp[0]=li[0]

if n>1:
	dp[1]=li[0]+li[1]
if n>2:
	dp[2]=max(li[0]+li[2],li[1]+li[2])

for i in range(2,n):
	#x o o
	s1=dp[i-3]+li[i-1]+li[i]
	#o x o
	s2=dp[i-2]+li[i]
	dp[i]=max(s1,s2)
print(dp[-1])
