import sys
n=int(input())
graph=[]
cnt=0
apt=[]

def dfs(x,y):
	global cnt

	if x<0 or x>=n or y<0 or y>=n:
		return 0

	if graph[x][y]==1:
		graph[x][y]=0
		cnt+=1

		dfs(x+1,y)
		dfs(x-1,y)
		dfs(x,y+1)
		dfs(x,y-1)
		return cnt
	return 0

for _ in range(n):
	graph.append(list(map(int,input().rstrip())))

for i in range(n):
	for j in range(n):
		if dfs(i,j):
			apt.append(cnt)
			cnt=0

print(len(apt))
apt.sort()
for i in apt:
	print(i)