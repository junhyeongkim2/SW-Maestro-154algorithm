import sys
sys.setrecursionlimit(5000)


def dfs(i, j):
    table[i][j] = 0
    dx = [1, 1, -1, -1, 1, -1, 0, 0]
    dy = [0, 1, 0, 1, -1, -1, 1, -1]
    for k in range(8):
        nx = dx[k] + i
        ny = dy[k] + j
        if 0 <= nx < h and 0 <= ny < w:
            if table[nx][ny] == 1:
                dfs(nx, ny)

            
            
    

while True:
    count = 0
    w, h = map(int, input().split())
    if(w == 0 and h == 0):
        break
    table = [list(map(int, input().split())) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if table[i][j] == 1:
                dfs(i, j)
                count+=1
    print(count)
