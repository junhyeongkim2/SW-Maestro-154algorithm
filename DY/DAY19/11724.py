# 11724번 연결 요소의 개수
# https://www.acmicpc.net/problem/11724

import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int, read().split())
visit = [False] * (N+1)

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
que = deque()
for i in range(1, N+1):
    if not visit[i]:
        que.append(i)
        visit[i] = True
        cnt += 1

    while que: # que가 빌 때까지
        p = que.popleft()
        for node in graph[p]: # p와 연결된 노드
            if not visit[node]:
                que.append(node)
                visit[node] = True
print(cnt)