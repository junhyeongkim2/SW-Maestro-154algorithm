#단지문제 (2차원 배열 -> 상하좌우 한 번에 다 살피기 )
import sys

total = int(input())
table = [list(sys.stdin.readline()) for _ in range(total)]

dx = [-1, 1, 0, 0 ]
dy = [0, 0, 1, -1]
def dfs(x, y):
    global count 
    table[x][y] = '0'
    count += 1
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if nx < 0 or ny < 0 or nx >= total or ny >= total:
            continue
        else:
            if table[nx][ny] == '1':
                dfs(nx, ny)
    
res = []

for i in range(total):
    for j in range(total):
        if table[i][j] == "1":
            count = 0
            dfs(i, j)
            res.append(count)

print(len(res))
for i in sorted(res):
    print(i)
        