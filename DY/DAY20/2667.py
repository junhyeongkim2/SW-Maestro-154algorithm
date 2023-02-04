# 2667번 단지번호붙이기
import sys
from collections import deque
read = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def BFS():
    cnt = 0 # 총 단지수
    house = list() # 각 단지내 집의 수 list
    for row in range(N):
        for col in range(N):
            if graph[row][col] == 1 and visited[row][col] == 0:
                que = deque([(row, col)])
                visited[row][col] = 1
                cnt += 1
                num = 1
                while que:  # que is not empty
                    y, x = que.popleft()
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx >= 0 and nx < N and ny >= 0 and ny < N and visited[ny][nx]==0 and graph[ny][nx]==1:
                            que.append((ny, nx))
                            visited[ny][nx] = 1
                            num += 1
                house.append(num)
    print(cnt)
    for n in sorted(house):
        print(n)

if __name__ == '__main__':
    N = int(read())
    graph = [list(map(int, read().strip())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    BFS()