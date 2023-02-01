import sys
input=sys.stdin.readline

n,c=map(int,input().split())
house=[int(input()) for _ in range(n)]
house.sort()

l=1
r=house[-1]-house[0]
ans=0

while l<=r:
	mid=(l+r)//2

	install=[]
	for i in house:
		if not install:
			install.append(i)
		elif i-install[-1]>=mid:
			install.append(i)

	if len(install)>=c:
		l=mid+1
		ans=mid
	else:
		r=mid-1
print(ans)