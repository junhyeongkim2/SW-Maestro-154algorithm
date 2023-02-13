import sys
read = sys.stdin.readline


def dfs(start):
    global idx, cur
    stack = list(graph[start])
    visit = [0]*(N+1)
    visit[start] = 1
    for g in graph[start]:
        visit[g[0]] = g[1]

    while stack:
        p_i, p_len = stack.pop()
        for g in graph[p_i]:
            i, l = g[0], g[1]
            if not visit[i]:
                visit[i] = visit[p_i]+l
                stack.append((i, l))
    cur = max(visit)
    idx = visit.index(cur)


N = int(read().strip())

if N==1:
    print(0)
    exit()

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    nodes = list(map(int,read().split()))
    parent = nodes[0]
    nodes = nodes[1:]
    for i in range(0, len(nodes)-1, 2):
        graph[parent].append((nodes[i], nodes[i+1]))
        graph[nodes[i]].append((parent, nodes[i + 1]))

cur = 0
idx = 0

dfs(1)
dfs(idx)
print(cur)