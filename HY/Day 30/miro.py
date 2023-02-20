from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())# N, M을 공백으로 구분하여 입력받기

graph = [] # 2차원 리스트의 맵 정보 입력받기
for i in range(n):
    graph.append(list(map(int, input().strip())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque() 
    q.append((x,y)) #0,0 담기
    
    while q: # 큐가 빌 때까지 반복
        x, y = q.popleft()
        for i in range(4):# 현재위치에서 상하좌우 확인
            nextX = x + dx[i] #새로 이동할 위치
            nextY = y + dy[i]
          
            if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:  #공간이탈 시 무시
                continue
            #벽인 경우 무시
            if graph[nextX][nextY] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nextX][nextY] == 1:
                graph[nextX][nextY] = graph[x][y] + 1 #지금까지 온 거리 +1
                q.append((nextX, nextY))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

# BFS를 수행한 결과 출력
print(bfs(0,0))