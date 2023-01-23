from collections import deque


def dfs(start):
    visited[start] = True
    for i in list[start]:
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in list[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                
        
        
    

n, m, p = map(int , input()) #노드, 간선, 시작 정점 
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for i in graph:
    i.sort()

visited = [False] * (n+1)

dfs(p)

# bfs
visited = [False] * (n + 1)
bfs(p)

