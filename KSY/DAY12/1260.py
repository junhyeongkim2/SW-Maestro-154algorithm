import queue

N, M, V = map(int, input().split())
edges = {}
visited = set()

stack = [V] #DFS
queue = queue.Queue() #BFS
queue.put(V)

#DFS
for _ in range(M):
    v1, v2 = map(int, input().split())
    edges[v1] = edges.get(v1, []) + [v2]
    # print(edges[v1])

answer = []
while stack:
    s = stack.pop()
    answer.append(s)

    if s in edges:
        edges[s].sort(reverse=True) #큰 수부터 stack에 넣어 작은 수 부터 꺼내기 위함
        for _s in edges[s]:
            if _s not in visited:
                stack.append(_s)
                visited.add(_s)

print(answer)