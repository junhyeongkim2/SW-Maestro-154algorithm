import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visit=[False]*(n+1)

for _ in range(m):
	u,v=map(int,input().split())
	graph[u].append(v)
	graph[v].append(u)

for i in graph:
	i.sort()

def dfs(n):
	visit[n]=True

	for i in graph[n]:
		if not visit[i]:
			visit[n]=True
			dfs(i)

cnt=0
for i in range(1,n+1):
	if not visit[i]:
		cnt+=1
		dfs(i)

print(cnt)