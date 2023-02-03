# 4963번 섬의 개수
import sys
from collections import deque
read = sys.stdin.readline

# 상하좌우 / 대각선
dx = [0, 0, -1, 1, -1, 1, -1, 1] # 열
dy = [-1, 1, 0, 0, -1, -1, 1, 1] # 행

def BFS():
    cnt = 0
    for row in range(h):
        for col in range(w):
            if graph[row][col] ==1 and visited[row][col] == 0: # 섬이면서 방문하지 않은 경우
                cnt += 1
                que = deque([(row, col)])
                visited[row][col] = 1 # 방문 표시
                while que:
                    y, x = que.popleft()
                    for i in range(8):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx >= 0 and nx < w and ny >= 0 and ny < h and visited[ny][nx] == 0 and graph[ny][nx] == 1:
                            que.append((ny, nx))
                            visited[ny][nx] = 1
    print(cnt)

if __name__ == '__main__':
    while True:
        w, h = map(int, read().split())
        if w == 0 and h == 0:  # 0 0 입력 시 종료
            break
        graph = [list(map(int, read().split())) for _ in range(h)]
        visited = [[0 for _ in range(w)] for _ in range(h)]
        BFS()
