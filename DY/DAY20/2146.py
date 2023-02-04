import sys
from collections import deque

read = sys.stdin.readline

N = int(read().strip())
graph = [list(map(int, read().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

que = deque()
boundary = deque()  # 섬 경계의 위치

num = 0
for r in range(N):  # 섬 분리 및 경계값 추출
    for c in range(N):
        if graph[r][c] == 1 and not visited[r][c]:
            num += 1
            b = list()
            que.append((r, c))
            graph[r][c] = num
            visited[r][c] = 1
            while que:
                x, y = que.popleft()
                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                        if graph[nx][ny] == 1:
                            que.append((nx, ny))
                            graph[nx][ny] = num
                            visited[nx][ny] = 1
                        else:
                            b.append((nx, ny))  # 경계값 저장
            boundary.append(b)

ans = 1000
for n in range(len(boundary) - 1):
    for i in range(len(boundary[n])):
        que.append(boundary[n][i])
        visited[que[0][0]][que[0][1]] = 1
        while que:
            x, y = que.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] == 0:
                        if (not visited[nx][ny] or visited[x][y] + 1 < visited[nx][ny]) and visited[x][y] + 1 < ans:
                            que.append((nx, ny))
                            visited[nx][ny] = visited[x][y] + 1

                    else:  # 섬의 가장자리인 경우
                        if (n + 1) != graph[nx][ny]:  # 다른 섬에 도착했을 경우에만 값 저장
                            ans = min(ans, visited[x][y])
print(ans)