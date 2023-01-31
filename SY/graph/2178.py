import sys
from collections import deque

n,m=map(int,input().split())
matrix=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
deq=deque([])
deq.append([0,0])

def bfs():
	while deq:
		v=deq.popleft()
		y=v[0]
		x=v[1]

		for i in range(4):
			ny=y+dy[i]
			nx=x+dx[i]

			if 0<=ny<n and 0<=nx<m and matrix[ny][nx]==1:
				matrix[ny][nx]=matrix[y][x]+1
				deq.append([ny,nx])

bfs()
print(matrix[n-1][m-1])
