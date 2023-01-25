#출발점이 여러 개 -> 미리 queue에 담기 
import sys
from collections import deque
input = sys.stdin.readline

w, h = map(int , input().split())
table = [list(map(int,input().split())) for _ in range(h)]
q = deque()

for i in range(h):
    for j in range(w):
        if table[i][j] == 1:
            q.append([i,j])
            
            
def bfs():
    
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = dx[k] + x
            ny = dy[k] + y
            if 0 <= nx < h and 0 <= ny < w and table[nx][ny] == 0:
                table[nx][ny] = table[x][y] + 1
                q.append((nx, ny))
                
                
    

bfs()

res = 0
for line in table:
    for tomato in line:
        if tomato == 0:
            print(-1)
            exit()
    res = max(res, max(line))

print(res-1)
    
        


            
