import sys
from collections import deque

n=int(input())
island=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
deq=deque([])
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for i in range(n):
	for j in range(n):
		if island[i][j]==1:
			for z in range(4):
				ny=i+dy[z]
				nx=j+dx[z]
				if 0<=nx<n and 0<=ny<n and island[ny][nx]==0:
					deq.append([ny,nx])


def bfs():
	while deq:
		deq2=deque([])
		deq2.append(deq.popleft())
		cnt=0
		while deq2:
			v=deq2.popleft()
			y=v[0]
			x=v[1]
			for i in range(4):
				ny=y+dy[i]
				nx=x+dx[i]
				if 0<=nx<n and 0<=ny<n:
					if island[ny][nx]==0:
						island[ny][nx]=island[y][x]-1
						cnt+=1
						deq2.append([ny,nx])
					else:
						break
		print('cnt',cnt)
bfs()
print()
for i in range(n):
	for j in range(n):
		print(island[i][j],end='   ')
	print()