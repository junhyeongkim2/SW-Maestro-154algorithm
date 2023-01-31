import sys
sys.setrecursionlimit(10**6)

n=int(sys.stdin.readline())
graph=[[] for _ in range(n+1)]
parent=[0 for _ in range(n+1)]
for _ in range(n-1):
	a,b=map(int,sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

for i in graph:
	i.sort()

def dfs(node):
	for i in graph[node]:
		if parent[i]==0:
			parent[i]=node
			dfs(i)
	return

dfs(1)
for i in parent[2:]:
	print(i)