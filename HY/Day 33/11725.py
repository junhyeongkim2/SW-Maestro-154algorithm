"""
트리의 부모 찾기 실버 2
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 
각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
graph = [[0] * (n+1) for _ in range(n*2)] #이런식의 이차원 이중배열은 너무 많은 메모리 소비                                                                                                                             
for i in range(n):
  x,y = map(int, input().split())
  graph[x][y] =1
  graph[y][x] =1
  """

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())

#그래프 만들기
graph = [[] for _ in range(n+1)]
for _ in range(n-1): #간선수는 n-1개
  x,y = map(int, input().split()) #[[1,2], [2,3] .....]
  graph[x].append(y)
  graph[y].append(x)
visited = [0] * (n+1)
#dfs 함수
def dfs(v):
    for i in graph[v]:
        if not visited[i]:  # 방문하지 않은 노드라면
            visited[i] = v #visited를 1이 아닌, 탐색을 시작한 값을 넣어준다 dfs는 항상 부모에서 자식으로 이동한다.
            dfs(i)  # 해당 노드를 시작 노드로 dfs

dfs(1)
#visited 출력
for i in range(2,n+1):
  print(visited[i])