from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                visited[i] = -visited[x]
                q.append(i)
            else:
                if visited[i] == visited[x]:
                    return False
    return True
            
total = int(input())
for _ in range(total):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n+1)
    flag = 1

    for _ in range(m):
        a, b = map(int , input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n+1):
        if visited[i] == 0:
            if not bfs(i):
                flag = -1
                break
    print('YES' if flag == 1 else 'NO')
                
        