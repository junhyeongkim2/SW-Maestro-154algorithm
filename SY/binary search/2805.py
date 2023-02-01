import sys
input=sys.stdin.readline

n,m=map(int,input().split())
h=list(map(int,input().split()))

l=1
r=max(h)

while l<=r:
	mid=(l+r)//2
	cnt=0

	for i in h:
		if i>=mid:
			cnt+=i-mid

	if cnt>=m:
		l=mid+1
	else:
		r=mid-1
print(r)