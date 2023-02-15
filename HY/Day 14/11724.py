import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)


n, m = map(int, input().split())
graph = [[i] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)  # 방문 여부 
cnt = 0  # 연결 요소 개수

# dfs 알고리즘(시작 노드)
def dfs(v):
    visited[v] = True  # 시작 노드 방문
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드라면
            dfs(i)  # 해당 노드를 시작 노드로 dfs

for i in range(1, n+1):
    if not visited[i]:  # 방문하지 않은 노드라면
        cnt += 1  # 연결요소를 하나 늘리고
        dfs(i)  # dfs탐색
print(cnt)
