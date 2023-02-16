# 순열 사이클

import sys

input = sys.stdin.readline
sys.setrecursionlimit(20000)


def dfs(start):
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


T = int(input())

for _ in range(T):
    cnt = 0
    N = int(input())
    arr = map(int, input().split())
    graph = [[] for i in range(N + 1)]

    visited = [False] * (N + 1)

    for i, a in enumerate(arr):
        graph[i + 1].append(a)

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1

    print(cnt)
