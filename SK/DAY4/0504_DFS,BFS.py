'''
미로 탈출
'''
from collections import deque

# Input
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# Define Variables
result = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
queue = deque([(0,0)])

# Algorithm
while queue:
    x, y = queue.popleft()
    for i in range(4):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        if tmp_x <= -1 or tmp_x >= n or tmp_y <= -1 or tmp_y >= m:
            continue
        else:
            if graph[tmp_x][tmp_y] == 1:
                graph[tmp_x][tmp_y] = graph[x][y] + 1
                queue.append((tmp_x, tmp_y))

# Outputs
print(graph[n-1][m-1])