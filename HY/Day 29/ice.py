""" 음료수 얼려먹기
dfs 알고리즘
세로 N과 가로 M
(1) 상하좌우를 살펴본 뒤, 주변 지점 중, '0'이며, 아직 방문하지 않았다면 방문 후 1로 넣어 구멍을 막아버림
(2) 방문한 지점에서 상하좌우를 살펴본 후, 방문을 진행하는 과정을 반복하면 연결된 모든 지점을
방문할 수 있다.
(3) 1~2를 반복하며, 방문 후, 카운트
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(x, y):
    if x <= -1 or y <= -1 or y >= m:  # 범위를 벗어나면 즉시 종료
        return False
    if graph[x][y] == 0:  # 만약 아직 방문을 안 한 구멍이면
        graph[x][y] == 1  # 방문처리, 구멍 막기
        print(graph[x][y])
        dfs(x - 1, y)  # 상
        dfs(x, y - 1)  # 좌
        dfs(x + 1, y)  # 우
        dfs(x, y + 1)  # 하
        return True
    else:
        return False


cnt = 0

for i in range(n):
    for j in range(m):
        if dfs(j, j) == True:
            cnt += 1
print(cnt)
