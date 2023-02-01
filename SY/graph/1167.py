"""
트리의 지름을 구하는 공식은
임의의 하나의 노드 A에서 가장 거리가 먼 노드 B를 구하고,
이 노드 B에서 가장 먼 노드 C를 구하게 되었을 때, 
B와 C 사이의 거리가 트리의 지름이 된다.
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n):
	tmp=list(map(int,input().split()))
	for i in range(1,len(tmp)-1,2):
		tree[tmp[0]].append([tmp[i],tmp[i+1]])

def dfs(n,d):
	for node, w in tree[n]:
		if dis[node]==-1:
			dis[node]=w+d
			dfs(node,w+d)

dis=[-1]*(n+1)
dis[1]=0 #출발지가 도착지가 될 수 없음
dfs(1,0)
mxnd=dis.index(max(dis))

dis=[-1]*(n+1)
dis[mxnd]=0 #출발지가 도착지가 될 수 없음
dfs(mxnd,0)

print(max(dis))