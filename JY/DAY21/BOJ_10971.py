import sys


def dfs(start,cur,cost):
    global matrix, visit, minCost

    #cur이 0일 때는 모든 경로를 돈 것이다. 최소 경로 비용을 계산한다. 
    if start == cur and visit.count(False) == 0:
        minCost = min(minCost, cost)

    
    for i in range(n):
        #0이면 방문할 수 없음 
        if not matrix[cur][i] == 0 and not visit[i]:
            visit[i] = True
            dfs(start,i,cost+matrix[cur][i])
            visit[i] = False


n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in sys.stdin.readline().split()])

# dfs
minCost = float('inf')
visit = [False for _ in range(n)]
dfs(0,0,0)

print(minCost)