import sys
sys.setrecursionlimit(100000) #백준 재귀 깊이(1000) 늘리기
def dfs(v):
	visit[v]=True

	for i in graph[v]:
		if not visit[i]:
			visit[i]=True
			dfs(i)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visit=[False]*(n+1)
cnt=0

for i in range(m):
	a,b=map(int,sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

for i in graph:
	i.sort()

for i in range(1,n+1):
	if not visit[i]:
		cnt+=1
		dfs(i)
print(cnt)