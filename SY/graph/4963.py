import sys
sys.setrecursionlimit(10**6)

def dfs(y,x):
	if x<0 or x>=w or y<0 or y>=h:
		return 0

	if graph[y][x]==1:
		graph[y][x]=0

		dfs(y+1,x)
		dfs(y-1,x)
		dfs(y,x+1)
		dfs(y,x-1)
		dfs(y+1,x+1)
		dfs(y-1,x+1)
		dfs(y+1,x-1)
		dfs(y-1,x-1)
		return 1
	return 0

while True:
	w,h=map(int,sys.stdin.readline().split())
	if w==0 and h==0:
		break

	graph=[list(map(int,sys.stdin.readline().split())) for _ in range(h)]
	cnt=0

	for i in range(h):
		for j in range(w):
			if dfs(i,j):
				cnt+=1
	print(cnt)
