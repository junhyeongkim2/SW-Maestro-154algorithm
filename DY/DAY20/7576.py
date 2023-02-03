# 7576번 토마토
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque
read = sys.stdin.readline

M, N = map(int, input().split()) # 가로/세로
tomatoes = [list(map(int, read().strip().split())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]
q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for row in range(N):
    for col in range(M):
        if tomatoes[row][col] == 1:
            q.append((row,col))

while q:
    p_x, p_y = q.popleft()

    for i in range(4):
        x = p_x + dx[i]
        y = p_y + dy[i]
        if x>=0 and x<N and y>=0 and y<M:
            if not visit[x][y] and tomatoes[x][y] == 0:
                q.append((x,y))
                tomatoes[x][y] = 1 # 익은 토마토를 1로 변경
                visit[x][y] = visit[p_x][p_y] + 1 # 일수 저장

for t in tomatoes:
    if t.count(0):  # 안 익은 게 있을 시
        print(-1)
        exit()

day = 0
for v in visit:
    day = max(day, max(v))
print(day)