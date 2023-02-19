import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(n):
	global cnt

	visit[n]=True
	cyc.append(n)

	v=li[n]

	if not visit[v]:
		dfs(v)
	elif v in cyc:
		cnt+=len(cyc[cyc.index(v):])
		return

for _ in range(int(input())):
	n=int(input())
	li=[0]+list(map(int,input().split()))
	visit=[False]*(n+1)
	cnt=0

	for i in range(1,n+1):
		if not visit[i]:
			cyc=[]
			dfs(i)

print(n-cnt)