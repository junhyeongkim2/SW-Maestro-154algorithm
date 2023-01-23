import sys

def twocnt(n):
	cnt=0
	while True:
		if n%2==0:
			cnt+=1
			n//=2
		else:
			return cnt

def fivecnt(n):
	cnt=0
	while True:
		if n%5==0:
			cnt+=1
			n//=5
		else:
			return cnt

n,m=map(int,sys.stdin.readline().split())
two,five=0,0
for i in range(2,n+1):
	two+=twocnt(i)
	five+=twocnt(i)
for i in range(2,n-m+1):
	two-=twocnt(i)
	five-=twocnt(i)
for i in range(2,m+1):
	two-=twocnt(i)
	five-=twocnt(i)
print(min(two,five))