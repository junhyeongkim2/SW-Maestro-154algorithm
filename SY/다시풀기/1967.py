import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(n,d):
	for v,c in tree[n]:
		if dis[v]==-1:
			dis[v]=c+d
			dfs(v,c+d)

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
	a,b,c=map(int,input().split())
	tree[a].append([b,c])
	tree[b].append([a,c])

dis=[-1]*(n+1)
dis[1]=0
dfs(1,0)
maxnode=dis.index(max(dis))

dis=[-1]*(n+1)
dis[maxnode]=0
dfs(maxnode,0)
print(max(dis))