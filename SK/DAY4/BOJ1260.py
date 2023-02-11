from collections import deque

# Input
n, m, v = map(int, input().split())

# Define variables
graph = [[]]* (n+1)
visited_dfs = [False]*(n+1)
visited_bfs = [False]*(n+1)

for _ in range(m):
    start, end = map(int, input().split())
    if graph[start] == []:
        graph[start] = [end]
    else:
        graph[start].append(end)
    if graph[end] == []:
        graph[end] = [start]
    else:
        graph[end].append(start)

for line in graph:
    line.sort()

# Define functions
def dfs(v):
    stack = [v]
    while stack:
        value = stack.pop()
        if not visited_dfs[value]:
            print(value, end=' ')
            visited_dfs[value] = True
            for i in graph[value]:
                if not visited_dfs[i]:
                    dfs(i)

def bfs(v):
    queue = deque([v])
    while queue:
        value = queue.popleft()
        if not visited_bfs[value]:
            print(value, end=' ')
            visited_bfs[value] = True
            for i in graph[value]:
                if not visited_bfs[i]:
                    queue.append(i)

# Algorithm
dfs(v)
print()
bfs(v)
