import sys
input=sys.stdin.readline

k,n=map(int,input().split())
lan=[int(input()) for _ in range(k)]
lan.sort()
l=1
r=max(lan)

while l<=r:
	cnt=0
	mid=(l+r)//2
	for i in lan:
		cnt+=i//mid

	if n>cnt:
		r=mid-1
	else:
		l=mid+1
print(r)
