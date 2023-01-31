"""
트리의 지름을 구하는 공식은
1. 임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고,
2. 이 노드 B에서 가장 먼 노드 C를 구하게 되었을 때, 
B와 C 사이의 거리가 트리의 지름이 된다.
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
	a,b,c=map(int,input().split())
	tree[a].append([b,c])
	tree[b].append([a,c])

def dfs(n,d):
	for node, w in tree[n]:
		if dis[node]==-1:
			dis[node]=w+d
			dfs(node,w+d)

#1번
dis=[-1]*(n+1)
dis[1]=0
dfs(1,0)

#2번
mxnd=dis.index(max(dis))
dis=[-1]*(n+1)
dis[mxnd]=0
dfs(mxnd,0)

print(max(dis))
