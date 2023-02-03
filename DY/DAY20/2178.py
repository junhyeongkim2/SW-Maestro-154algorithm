# 2178번 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(map(int, read().strip())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
visit[0][0] = 1

dx = [-1, 1, 0, 0] # 행
dy = [0, 0, -1, 1] # 열
q = deque()
q.append((0,0))

while q: # q가 빌 때까지 계속 진행
    p_x, p_y = q.popleft()
    for i in range(4):
        x = p_x + dx[i]
        y = p_y + dy[i]
        if x >= 0 and x < N and y >= 0 and y < M:
            if not visit[x][y] and maze[x][y]: # 방문하지 않고, 이동할 수 있는 경우
                q.append((x,y))
                visit[x][y] = visit[p_x][p_y] + 1
print(visit[N-1][M-1])