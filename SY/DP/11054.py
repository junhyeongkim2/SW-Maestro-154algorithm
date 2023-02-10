n=int(input())
li=list(map(int,input().split()))
indp=[1]*n
dedp=[1]*n
dp=[0]*n

for i in range(n):
	for j in range(i):
		if li[j]<li[i]:
			indp[i]=max(indp[i],indp[j]+1)

li.reverse()
for i in range(n):
	for j in range(i):
		if li[j]<li[i]:
			dedp[i]=max(dedp[i],dedp[j]+1)
dedp.reverse()

for i in range(n):
	dp[i]=indp[i]+dedp[i]-1
print(max(dp))