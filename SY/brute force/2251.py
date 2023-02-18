from collections import deque
import sys
input=sys.stdin.readline

a,b,c=map(int,input().split())
ans=[]
visit=[[False]*(a+1) for _ in range(b+1)]
deq=deque()
deq.append([0,0])
visit[0][0]=True

def pour(x,y):
	if not visit[y][x]:
		visit[y][x]=True
		deq.append([x,y])

def bfs():
	while deq:
		print(deq)
		x,y=deq.popleft()
		z=c-x-y

		if x==0:
			ans.append(z)

		#a->b
		w=min(x,b-y)
		pour(x-w,y+w)

		#a->c
		w=min(x,c-z)
		pour(x-w,y)

		#b->a
		w=min(y,a-x)
		pour(x+w,y-w)

		#b->c
		w=min(y,c-z)
		pour(x,y-w)

		#c->a
		w=min(z,a-x)
		pour(x+w,y)

		#c->b
		w=min(z,b-y)
		pour(x,y+w)

bfs()

ans.sort()
for i in ans:
	print(i,end=' ')

