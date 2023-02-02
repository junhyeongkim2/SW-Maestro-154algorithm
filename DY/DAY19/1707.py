# 1707 이분 그래프
# https://www.acmicpc.net/problem/1707

# 방문한 순서에 따라 번호를 메기고, 만약 이전에 방문한 정점인 경우 새로운 번호와 이전의 번호가 짝수만큼 차이나지 않는 경우 이분 그래프가 아니라고 판단하여 풀이했다.

# 처음에 아래 사실을 간과하여 node 1번에 대해서만 확인했다가 다음과 같은 예제가 통과되지 않았다. (50% 틀렸습니다.)
# 1
# 4 3
# 2 3
# 3 4
# 4 2

# 비연결 그래프일 수 있다.
# 1번 정점에서만 탐색을 해서는 안 됩니다.
# 1번 정점과 연결되지 않은 다른 정점들 사이에서 이분 그래프를 못 만들 수 있습니다.
# 1번 뿐만 아니라, 어느 정점이라도 마찬가지입니다. 주어지는 그래프는 연결 그래프가 아닐 수 있습니다.

import sys
from collections import deque
read = sys.stdin.readline

T = int(read().strip())
for _ in range(T): # Test case
    V, E = map(int, read().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, read().split())
        graph[u].append(v)
        graph[v].append(u)

    if V==1:
        print("YES")
        continue

    access = [False] * (V+1)
    for node in range(1, V+1):
        if access[node]: continue
        visit = [0]*(V+1)
        que = deque([node])
        visit[node]=1
        access[node] = True

        res = False # 결과 출력 유무
        while que:
            p = que.popleft()
            for g in graph[p]:
                if not visit[g]:
                    access[g] = True
                    visit[g] = visit[p] + 1
                    que.append(g)
                else:
                    if visit[g]%2 != (visit[p]+1)%2:
                        print("NO")
                        res = True
                        que.clear()
                        break
        if res: break
    if not res:  # 결과가 아직 출력되지 않은 경우
        print("YES")
