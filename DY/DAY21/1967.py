import sys
from collections import deque
read = sys.stdin.readline

def tree_radius(nodes):
    radius = list()
    visit = [0] * (N+1)
    for node in nodes:
        max_r = 0
        que = deque([node])
        visit[node[0]]=node[1]
        while que:
            n, r = que.pop()
            if len(graph[n]) == 0:  # leaf node인 경우
                max_r = max(max_r, visit[n])
            for g in graph[n]:
                que.append(g)
                visit[g[0]]=visit[n]+g[1]
        radius.append(max_r)
    radius.sort()
    return radius[-1]+radius[-2]

def tree_radius_2(nodes):
    radius = list()
    visit = [0] * (N+1)
    for node in nodes:
        max_r = 0
        que = deque([node])
        visit[node[0]]=node[1]
        while que:
            n, r = que.pop()
            if len(graph[n]) == 0:  # leaf node인 경우
                max_r = max(max_r, visit[n])
            for g in graph[n]:
                que.append(g)
                visit[g[0]]=visit[n]+g[1]
        radius.append(max_r)
    radius.sort()
    return radius[-1]

N = int(read().strip())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    g = list(map(int, read().split()))
    graph[g[0]].append(g[1:])

# root 자식 1개일 때 예외 처리 필요

base = 0
ans = 0
if len(graph[1])==1: # 1의 자식이 1개인 경우
    ans = tree_radius_2(graph[1])

for i in range(1, N+1):
    if len(graph[i]) >= 2:
        ans = max(ans,tree_radius(graph[i]))
print(ans)