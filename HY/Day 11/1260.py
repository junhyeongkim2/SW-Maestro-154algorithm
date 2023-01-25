from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
  x, y = map(int, input().split())
  [x][y] = 1
  [y][x] = 1

#방문 여부를 담은 리스트
dfs_visted = [0] * n + 1
bfs_visted = [0] * n + 1


#DFS 알고리즘 함수
def dfs(v):
  #방문 처리
  dfs_visted[v] = 1
  #방문한 순서대로 노드 출력
  print(v, end=" ")
  #next는 이동할 다음 노드를 뜻함
  for next in range(1, n + 1):
    #방문기록이 없고, 인덱스에 next 값이 있다면(연결되어 갈 수 있다면)
    if dfs_visted[next] == 0 and graph[v][next] == 1:
      #방문한다. 재귀함수 이용
      dfs(next)
      #호출될 때마다 visted는 1이되고 14번째 코드에서 재귀되어 v에 next값이 들어간다


#BFS 알고리즘 함수
def bfs(v):
  q = deque([v])  #값을 담을 q

  while q:  # q가 빌때까지 돈다.
    cur = q.popleft(0)  # q에 있는 첫번째 값 꺼낸다.
    print(cur, end=" ")  # 해당 값 출력
    for next in range(1, n + 1):
      # 방문기록이 없고 인덱스에 next 값이 있다면(연결되어 갈 수 있다면)
      if bfs_visted[next] == 0 and graph[v][next] == 1:
        q.append(next)  #q에 next를 추가
        bfs_visted[next] = 1  #  #방문 처리


dfs(v)
print()
bfs(v)
