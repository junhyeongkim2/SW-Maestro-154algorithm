import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int, input().split())
table = []
for _ in range(A):
    table.append(input().rstrip())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [["" for _ in range(B)]  for _ in range(A)]

def bfs():
    global ans
    qu = deque()
    qu.append([0, 0, table[0][0]])
    visited[0][0] = table[0][0]
    while qu:
        x, y, v = qu.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < A and 0 <= ny < B and table[nx][ny] not in v:
                if visited[nx][ny] != v+table[nx][ny]: #그냥 참거짓으로 하면 다시 돌아올 수 없다. -> 그냥 그동안 왔던 경로를 저장하자 
                    visited[nx][ny] = v+table[nx][ny]
                    qu.append([nx, ny, v+table[nx][ny]])
                    
    return len(v)
                


print(bfs())
                    
                
        



    