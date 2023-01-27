def dfs(start):
    visited[start] = True
    next = graph[start]
    if visited[next] == False:
        dfs(next)
    
for i in range(int(input())):
    num = int(input())
    visited = [False]*(num+1)
    graph = [0] + list(map(int, input().split()))
    count = 0
    for i in range(1, num+1):
        if visited[i] == False:
            dfs(i)
            count +=1
    print(count)