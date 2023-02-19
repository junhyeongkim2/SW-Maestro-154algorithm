import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(n):
	global ans

	visit[n]=True

	for i in graph[n]:
		if not visit[i]:
			visit[i]=True
			color[i]=int(not color[n])
			dfs(i)
		elif color[n]==color[i]:
			ans=0

for _ in range(int(input())):
	n,e=map(int,input().split())
	graph=[[] for _ in range(n+1)]
	visit=[False]*(n+1)
	color=[0]*(n+1)
	ans=1

	for _ in range(e):
		u,v=map(int,input().split())
		graph[u].append(v)
		graph[v].append(u)

	for i in graph:
		i.sort()

	for i in range(1,n+1):
		dfs(i)

	if ans:
		print("YES")
	else:
		print("NO")