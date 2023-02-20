import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(x,y):
	island[y][x]=0

	for i in range(8):
		ny=y+dy[i]
		nx=x+dx[i]

		if 0<=nx<w and 0<=ny<h and island[ny][nx]==1:
			dfs(nx,ny)

while True:
	w,h=map(int,input().split())
	if w==0 and h==0:
		break

	island=[list(map(int,input().split())) for _ in range(h)]
	dy=[-1,1,0,0,1,1,-1,-1]
	dx=[0,0,-1,1,-1,1,-1,1]
	cnt=0

	for i in range(h):
		for j in range(w):
			if island[i][j]==1:
				dfs(j,i)
				cnt+=1

	print(cnt)