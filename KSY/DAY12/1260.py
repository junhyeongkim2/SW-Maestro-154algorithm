import queue

N, M, V = map(int, input().split())
edges = {}

stack = [V] #DFS
queue = queue.Queue() #BFS
queue.put(V)

#DFS
for _ in range(M):
    v1, v2 = map(int, input().split())
    edges[v1] = edges.get(v1, []) + [v2]
    edges[v2] = edges.get(v2, []) + [v1]
    # print(edges[v1])

answer = ""
visited = set()
while stack:
    s = stack.pop()
    if s not in visited:
        answer += str(s) + " "
        visited.add(s)

        if s in edges:
            edges[s].sort(reverse=True) #큰 수부터 stack에 넣어 작은 수 부터 꺼내기 위함
            for _s in edges[s]:
                if _s:
                    stack.append(_s)

print(answer)

answer = ""
visited = set()
while not queue.empty(): #queue는 list처럼 내용이 없으면 0을 뱉지 않음.
    q = queue.get()
    if q not in visited:
        answer += str(q) + " "
        visited.add(q)

        if q in edges:
            edges[q].sort()
            for _q in edges[q]:
                queue.put(_q)

print(answer)