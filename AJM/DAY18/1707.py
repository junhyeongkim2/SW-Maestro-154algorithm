# 이분 그래프

import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def dfs(start, group):
    global error

    if error:
        return

    visited[start] = group

    for i in graph[start]:
        if visited[i] == False:
            dfs(i, -group)
        elif visited[start] == visited[i]:
            error = True
            return


k = int(input())

for i in range(k):
    v, e = map(int, input().split())
    error = False
    graph = [[] for _ in range(v + 1)]
    visited = [False] * (v + 1)

    for j in range(e):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    for j in range(1, v + 1):
        if visited[j] == False:
            dfs(j, 1)
            if error:
                break
    if error:
        print("NO")
    else:
        print("YES")
