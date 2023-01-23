import sys
sys.setrecursionlimit(10**6)

def dfs(v):
	global tmp

	visit[v]=True
	for i in graph[v]:
		if not visit[i]:
			visit[i]=True
			color[i]=int(not color[v])
			dfs(i)
		else:
			if color[v]==color[i]:
				tmp=0

k=int(input())
for i in range(k):
	v,e=map(int,input().split())
	graph=[[] for _ in range(v+1)]
	visit=[False]*(v+1)
	color=[0]*(v+1)
	tmp=1

	for i in range(e):
		a,b=map(int,sys.stdin.readline().split())
		graph[a].append(b)
		graph[b].append(a)
	for i in graph:
		i.sort()

	for i in range(1,v+1):
		dfs(i)
	if tmp:
		print('YES')
	else:
		print('NO')
