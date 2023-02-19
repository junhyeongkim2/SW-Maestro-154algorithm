from collections import deque

def bfs():
	while deq:
		x,y=deq.popleft()

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]

			if 0<=nx<m and 0<=ny<n and box[ny][nx]==0:
				box[ny][nx]=box[y][x]+1
				deq.append([nx,ny])

m,n=map(int,input().split())
box=[list(map(int,input().split())) for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
deq=deque()
ans=0

for i in range(n):
	for j in range(m):
		if box[i][j]==1:
			deq.append([j,i])

bfs()

for i in box:
	for j in i:
		if j==0:
			print(-1)
			exit()
		ans=max(ans,j)
print(ans-1)