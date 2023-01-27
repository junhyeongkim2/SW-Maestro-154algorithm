import sys
from collections import deque
input = sys.stdin.readline

h, w = map(int, input().split())
table = []
for _ in range(h):
    table.append(list(map(int, input().rstrip())))
q = deque()

def bfs():
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0 , -1]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < h and 0 <= ny < w and table[nx][ny] == 1:
                table[nx][ny] = table[x][y] + 1
                q.append((nx, ny))
        
        
q.append([0, 0])
bfs()

print(table[h-1][w-1])


