"""
미로찾기
 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 
 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 
 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

"""

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
            #범위를 벗어나면
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
