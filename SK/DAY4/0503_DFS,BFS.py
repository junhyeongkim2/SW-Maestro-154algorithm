'''
음료수 얼려 먹기
'''

# Input
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

# Define Variables
result = 0

# Define functions
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
# Algorithm
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

# Output
print(result)