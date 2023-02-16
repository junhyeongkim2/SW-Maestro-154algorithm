from collections import deque

n, m = map(int,input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx==0 and ny==0 
      nx = x + dx[i]
      ny = y + dy[i]

      if not (0 <= nx < n and 0 <= ny < m):
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] += graph[x][y]
        queue.append((nx, ny))
    
  return graph[n-1][m-1]


print(bfs(0, 0))