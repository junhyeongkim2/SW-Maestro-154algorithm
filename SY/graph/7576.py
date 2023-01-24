import sys
from collections import deque

def bfs():
	while deq:
		v=deq.popleft()
		y=v[0]
		x=v[1]

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]
			if 0<=nx<m and 0<=ny<n and box[ny][nx]==0:
				box[ny][nx]=box[y][x]+1
				deq.append([ny,nx])

m,n=map(int,input().split())
box=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
deq=deque([])
dx=[0,0,-1,1]
dy=[-1,1,0,0]
day=0

for i in range(n):
	for j in range(m):
		if box[i][j]==1:
			deq.append([i,j])
bfs()

for i in range(n):
	for j in range(m):
		if box[i][j]==0:
			print(-1)
			exit()
		day=max(day,box[i][j])
print(day-1)