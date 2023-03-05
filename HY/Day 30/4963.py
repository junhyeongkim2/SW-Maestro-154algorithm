"""
DFS 섬의 개수 실버 2

"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, 1, -1, -1, 1]


def dfs(x, y):
    if 0 <= x < h and 0 <= y < w and graph[x][y] == 1:
        graph[x][y] = 0
        for i in range(8):
            nextX = dx[i] + x
            nextY = dy[i] + y
            dfs(nextX, nextY)
        return True
    return False


while True:
    # 너비w 높이h
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 0이 입력되면 break
        break
    # h까지  map 만들기
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
