import sys
from collections import deque

def D(n):
	return (2*n)%10000

def S(n):
	if n==0:
		return 9999
	else:
		return (n-1)%10000

def L(n):
	return 10*(n%1000)+n//1000

def R(n):
	return 1000*(n%10)+n//10

def bfs(m):
	while deq:
		v,ans=deq.popleft()
		if v==m:
			return ans

		num=D(v)
		if not visit[num]:
			tmp=ans+"D"
			deq.append([num,tmp])
			visit[num]=1

		num=L(v)
		if not visit[num]:
			tmp=ans+"L"
			deq.append([num,tmp])
			visit[num]=1

		num=R(v)
		if not visit[num]:
			tmp=ans+"R"
			deq.append([num,tmp])
			visit[num]=1

		num=S(v)
		if not visit[num]:
			tmp=ans+"S"
			deq.append([num,tmp])
			visit[num]=1

for _ in range(int(input())):
	n,m=map(int,input().split())
	visit=[False for _ in range(10000)]
	visit[n]=1
	deq=deque()
	deq.append([n,""])
	print(bfs(m))
