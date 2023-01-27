import sys
sys.setrecursionlimit(10**6)

def dfs(i):
	global cnt
	visit[i]=True
	cyc.append(i)

	v=li[i]
	if not visit[v]:
		dfs(v)
	elif v in cyc:
		cnt+=len(cyc[cyc.index(v):])
		return

for _ in range(int(input())):
	n=int(sys.stdin.readline())
	li=[0]+list(map(int,sys.stdin.readline().split()))
	visit=[False]*(n+1)
	cnt=0

	for i in range(1,n+1):
		if not visit[i]:
			cyc=[]
			dfs(i)

	print(n-cnt)