import sys
sys.setrecursionlimit(2000)

def dfs(v):
	visit[v]=True
	if v not in cyc:
		cyc.append(v)

	for i in graph[v]:
		if not visit[i]:
			visit[i]=True
			cyc.append(i)
			dfs(i)

t=int(input())
for i in range(t):
	n=int(input())
	li=list(map(int,sys.stdin.readline().split()))
	graph=[[] for _ in range(n+1)]
	visit=[False]*(n+1)
	cnt=0

	for i in range(n):
		if i+1==li[i]:
			cnt+=1
			continue
		graph[i+1].append(li[i])
		graph[li[i]].append(i+1)
	for i in graph:
		i.sort()

	for i in range(1,n+1):
		cyc=[]
		dfs(i)
		if cyc[-1] in graph[cyc[0]]:
			cnt+=1
	print(cnt)