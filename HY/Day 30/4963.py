"""
DFS 섬의 개수 실버 2

"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(x, y):
    if x < 0 or y < 0 or y >= w or x >= h:  # 범위를 벗어나면 False 반환
        return False
        # 상, 하, 좌, 우의 위치도 모두 탐색해서 다 0이면 1로 바다로 만들어버림
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)  # 상하좌우 대각선도 탐색
        dfs(x-1, y-1)
        dfs(x, y-1)
        dfs(x+1, y-1)
        dfs(x+1, y)
        dfs(x+1, y+1)
        dfs(x, y+1)
        dfs(x-1, y+1)
        return True
    return False

while True:
    # 너비w 높이h
    w, h = map(int, input().split())
    if w == 0 and h == 0: #0이 입력되면 break
        break
    #h까지  map 만들기 
    graph = []
    for i in range(h): 
        graph.append(list(map(int, input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            # dfs 실행 후 True를 받아오면
            if dfs(i, j) == True:
                result += 1
    print(result)
