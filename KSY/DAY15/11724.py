import sys

input = sys.stdin.readline
sys.setrecursionlimit(5000)  # 시스템 재귀 횟수 설정

N, M = map(int, input().split())
edges = {}
visited = [False] * (N + 1)  # 경유한 vertexes
component = 0

# edge 연결
for _ in range(M):
    v1, v2 = map(int, input().split())
    # 각 정점에 대해서 방향을 가지지 않으므로 두 방향 다 추가 해 주어야 한다.
    edges[v1] = edges.get(v1, []) + [v2]
    edges[v2] = edges.get(v2, []) + [v1]


def dfs(v):
    visited[v] = True  # 방문 표시
    for edge in edges[v]:  # 해당 vertex의 edge모두 삽입
        if not visited[edge]:  # 한 번 방문한 vertex는 stack에 넣지 않는다
            dfs(edge)


for v in range(1, N + 1):  # 아직 방문 하지 않은 vertex 선택하기 edges에만 있는 원소로 돌면 안 됨
    if not visited[v]:
        if v not in edges:
            visited[v] = True  # 해당 정점에 edge가 없다면 방문 표시만
        else:
            dfs(v)  # 선택한 vertex에 대해서 dfs
        component += 1

print(component)
