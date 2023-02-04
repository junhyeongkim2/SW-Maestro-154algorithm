import sys
input = sys.stdin.readline

total = int(input())
arr = []
for _ in range(total):
    arr.append(list(map(int, input().split())))
visited = [False] * (total)
ans = sys.maxsize

def dfs(start, cur, cost):
    if start == cur and visited[i] == False:
        ans = min(ans, cost)
    for i in range(total):
        if not arr[cur][i] and visited[i] == False:
            visited[i] == True
            dfs(start, i, cost+arr[cur][i])
            visited[i] = False

dfs(0, 0, 1)
print(ans)
            
        
    