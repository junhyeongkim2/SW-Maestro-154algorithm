import sys

sys.setrecursionlimit(5000)

n, m = map(int , input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    visited[start] = True
    for i in graph[start]:
        if visited[i] == False:
            bfs(i)
    

visited = [False] * (n + 1)

count = 0
for i in range(1, n+1):
    if visited[i] == False:
        if not graph[i]:
            count += 1
            visited[i] = True
        else:
            bfs(i)
            count += 1
    
print(count)
