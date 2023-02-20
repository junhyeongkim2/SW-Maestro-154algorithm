def dfs(x,y):
	global cnt

	house[y][x]=0
	cnt+=1

	for i in range(4):
		ny=y+dy[i]
		nx=x+dx[i]

		if 0<=nx<n and 0<=ny<n and house[ny][nx]==1:
			dfs(nx,ny)

n=int(input())
house=[list(map(int,input())) for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
dan=[]

for i in range(n):
	for j in range(n):
		if house[i][j]==1:
			cnt=0
			dfs(j,i)
			dan.append(cnt)

dan.sort()
print(len(dan))
for i in dan:
	print(i)
