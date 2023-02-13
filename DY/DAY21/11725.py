import sys
from collections import deque
read = sys.stdin.readline

N = int(read().strip())
graph = [[] for _ in range(N+1)]
visit = [0]*(N+1)

for _ in range(N-1):
    u, v = map(int, read().split())
    graph[u].append(v)
    graph[v].append(u)

que = deque([1])
for i in range(1, N+1):
    if visit[i]: break # 이미 방문한 경우 다음으로 넘어감
    while que:
        p_que = que.popleft()
        for g in graph[p_que]:
            if not visit[g]:
                que.append(g)
                visit[g] = p_que

for num in visit[2:]:
    print(num)