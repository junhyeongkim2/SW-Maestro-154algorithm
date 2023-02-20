from collections import deque
import sys

def island_bfs(x,y):
	global cnt

	island[y][x]=cnt
	deq.append([x,y])
	visit[y][x]=True

	while deq:
		x,y=deq.popleft()

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]

			if 0<=nx<n and 0<=ny<n and not visit[ny][nx] and island[ny][nx]==1:
				island[ny][nx]=cnt
				visit[ny][nx]=True
				deq.append([nx,ny])

def brdg_bfs(k):
	global dis

	deq=deque()
	brdg=[[-1]*n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			if island[i][j]==k:
				brdg[i][j]=0
				deq.append([j,i])

	while deq:
		x,y=deq.popleft()

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]

			if 0<=nx<n and 0<=ny<n:
				if brdg[ny][nx]==-1 and island[ny][nx]==0:
					brdg[ny][nx]=brdg[y][x]+1
					deq.append([nx,ny])
				if island[ny][nx]>0 and island[ny][nx]!=k:
					dis=min(dis,brdg[y][x])
					return

n=int(input())
island=[list(map(int,input().split())) for _ in range(n)]
visit=[[False]*n for _ in range(n)]
deq=deque()
dy=[-1,1,0,0]
dx=[0,0,-1,1]
cnt=1
dis=sys.maxsize

for i in range(n):
	for j in range(n):
		if island[i][j]==1 and not visit[i][j]:
			island_bfs(j,i)
			cnt+=1

for i in range(1,cnt):
	brdg_bfs(i)

print(dis)