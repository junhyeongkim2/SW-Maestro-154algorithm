import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8) #재귀 함수를 사용할 때 리미트를 걸어줘야함

#입력 및 그래프 생성, 인접 리스트 방식 사용
n, m = map(int, input().split())
graph = [[i] for i in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)  # 방문 여부 
cnt = 0  # 연결 요소 개수

# dfs 알고리즘(탐색할 그래프, 시작 노드, 방문여부 리스트)
def dfs(graph, start, visited):
    visited[start] = True  # 시작 노드 방문
    for i in graph[start]:
        if not visited[i]:  # 방문하지 않은 노드라면
            dfs(graph, i, visited)  # 해당 노드를 시작 노드로 dfs


for i in range(1, n+1):
    if not visited[i]:  # 방문하지 않은 노드라면
        cnt += 1  # 연결요소를 하나 늘리고
        dfs(graph, i, visited)  # dfs탐색
print(cnt)
