from collections import deque

def dfs(v):
	dvisit[v]=True
	print(v,end=' ')

	for i in graph[v]:
		if not dvisit[i]:
			dfs(i)

def bfs(start):
	deq=deque([start])
	bvisit[start]=True

	while deq:
		v=deq.popleft()
		print(v,end=' ')

		for i in graph[v]:
			if not bvisit[i]:
				deq.append(i)
				bvisit[i]=True

n,m,v=map(int,input().split())
graph=[[] for _ in range(n+1)]
dvisit=[False]*(n+1)
bvisit=[False]*(n+1)

#입력
for i in range(m):
	a,b=map(int,input().split())
	graph[a].append(b)
	graph[b].append(a)
#정렬
for i in graph:
	i.sort()

dfs(v)
print()
bfs(v)