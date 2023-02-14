import sys
input=sys.stdin.readline

n,k=map(int,input().split())
cost=[int(input()) for _ in range(n)]
cost.reverse()
cnt=0

while k:
	for i in cost:
		if i<=k:
			cnt+=(k//i)
			k-=i*(k//i)
print(cnt)