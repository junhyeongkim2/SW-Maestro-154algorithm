import sys
input=sys.stdin.readline

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=a+b
c.sort()

for i in c:
	print(i,end=' ')
