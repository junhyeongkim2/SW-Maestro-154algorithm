# 1260
import sys
from collections import deque

def DFS(start): # dfs search
    visit[start] = True # visit check
    print(start, end=' ')

    for i in graph[start]:
        if not visit[i]: # never visited
            DFS(i)

def BFS(start): # dfs search
    que = deque([start]) # que create
    visit[start] = True # visit check

    while que: # que is not empty
        node = que.popleft()
        print(node, end=' ')

        for i in graph[node]:
            if not visit[i]: # never visited
                que.append(i)
                visit[i] = True


if __name__ == '__main__':
    input = sys.stdin.readline
    n, m, v = map(int, input().split())

    graph = [[] for _ in range(n + 1)]  # graph create
    for _ in range(m):  # graph initialization
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, n + 1):
        graph[i].sort()

    visit = [0 for _ in range(n + 1)]  # visit list create
    DFS(v)
    print()

    visit = [0 for _ in range(n + 1)]  # visit list create
    BFS(v)