import sys
from collections import deque

n=int(input())
island=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit=[[False]*n for _ in range(n)]
dis=sys.maxsize
cnt=1
dy=[-1,1,0,0]
dx=[0,0,-1,1]

#각각의 섬을 구분하기
def bfs(y,x):
	global cnt

	deq=deque([])
	deq.append([y,x])
	visit[y][x]=True
	island[y][x]=cnt

	while deq:
		v=deq.popleft()
		y=v[0]
		x=v[1]

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]
			if 0<=nx<n and 0<=ny<n:
				if island[ny][nx]==1 and not visit[ny][nx]:
					deq.append([ny,nx])
					island[ny][nx]=cnt
					visit[ny][nx]=True

#섬과 섬 사이의 최단 거리 구하기
def bfs2(k):
	global dis

	deq=deque([])
	route=[[-1]*n for _ in range(n)]

	for i in range(n):
		for j in range(n):
			if island[i][j]==k:
				deq.append([i,j])
				route[i][j]=0
	print(deq)
	while deq:
		v=deq.popleft()
		y=v[0]
		x=v[1]

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]
			if 0<=nx<n and 0<=ny<n:
				if island[ny][nx]==0 and route[ny][nx]==-1:
					route[ny][nx]=route[y][x]+1
					deq.append([ny,nx])
					print(deq)
				if island[ny][nx]>0 and island[ny][nx]!=k:
					dis=min(dis,route[y][x])
					return
				for i in range(n):
						for j in range(n):
							print(route[i][j],end=' ')
						print()

for i in range(n):
	for j in range(n):
		if island[i][j]==1 and not visit[i][j]:
			bfs(i,j)
			print()
			cnt+=1

for i in range(1,2):
		bfs2(i)

print(dis)
