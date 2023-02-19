from collections import deque

def bfs():
	while deq:
		x,y=deq.popleft()

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]

			if 0<=nx<m and 0<=ny<n and mrx[ny][nx]==1:
				mrx[ny][nx]=mrx[y][x]+1
				deq.append([nx,ny])

n,m=map(int,input().split())
mrx=[list(map(int,input())) for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
deq=deque()
deq.append([0,0])

bfs()

print(mrx[n-1][m-1])