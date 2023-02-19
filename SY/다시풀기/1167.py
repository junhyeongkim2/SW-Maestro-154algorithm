"""
트리의 지름을 구하는 공식은
임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고,
이 노드 B에서 가장 먼 노드 C를 구하게 되었을 때, 
B와 C 사이의 거리가 트리의 지름이 된다.
"""
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

for _ in range(n):
	li=list(map(int,input().split()))

	for i in range(1,len(li)-1,2):
		tree[li[0]].append([li[i],li[i+1]])

dis=[-1]*(n+1)
dis[1]=0
dfs(1,0)
maxnode=dis.index(max(dis))

dis=[-1]*(n+1)
dis[maxnode]=0
dfs(maxnode,0)
print(max(dis))