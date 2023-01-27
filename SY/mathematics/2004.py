import sys
def twocnt(n):
	cnt=0
	i=2
	while n//i>0:
		cnt+=n//i
		i*=2
	return cnt

def fivecnt(n):
	cnt=0
	i=5
	while n//i>0:
		cnt+=n//i
		i*=5
	return cnt

n,m=map(int,sys.stdin.readline().split())

two=twocnt(n)-twocnt(n-m)-twocnt(m)
five=fivecnt(n)-fivecnt(n-m)-fivecnt(m)
print(min(two,five))