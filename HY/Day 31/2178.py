import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []

for i in range(n):
    maps.append(list(map(int, input().strip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q = deque()
    q.append((0,0)) #초기값 0 0 넣어줌
    
    while q:
        x,y =q.popleft() #★★★★★★★★★★★★★★★★★★★
        for i in range(4):
            nextX = x + dx[i] #다음으로 이동할 좌표들
            nextY = y + dy[i]

            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
                continue
            #노드가 0이라면 ★★★★★★★★★★★★★★★★★★★★★★★★
            if maps[nextX][nextY] == 0:
                continue
            if maps[nextX][nextY] == 1:
                maps[nextX][nextY] = maps[x][y] + 1  #노드값을 +1
                q.append((nextX, nextY))
    return maps[-1][-1]

print(bfs())
