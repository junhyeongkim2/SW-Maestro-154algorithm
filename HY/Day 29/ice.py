""" 음료수 얼려먹기
dfs 알고리즘
세로 N과 가로 M
(1) 상하좌우를 살펴본 뒤, 주변 지점 중, '0'이며, 
아직 방문하지 않았다면 방문 후 1로 넣어 구멍을 막아버림
(2) 방문한 지점에서 상하좌우를 살펴본 후, 방문을 진행하는 과정을 반복하면 연결된 모든 지점을
방문할 수 있다.
(3) 1~2를 반복하며, 방문 후, 카운트
"""
import sys
sys.stdin.readline
sys.setrecursionlimit(10 ** 8) #재귀 함수를 사용할 때 리미트를 걸어줘야함

n,m = map(int,input().split())
graph =[]

for i in range(n):
   graph.append(list(map(int,input())))

def dfs(x,y):
    # 범위를 벗어나면 즉시 종료
   if x <= -1 or x >= n or y <= -1 or y >= m:
       return False
   if graph[x][y] == 0: # 만약 아직 방문을 안 한 구멍이면
       graph[x][y] = 1  # 구멍 막고, 
       # 상, 하, 좌, 우의 위치도 모두 탐색해서 다 0이면 1로 구멍막음
       dfs(x-1,y)
       dfs(x,y-1)
       dfs(x+1,y)
       dfs(x,y+1)
       return True # 채울 공간 1개 완성~
   return False  # 1이면 False 

#모든 노드에 대하여 음료수 채우기
result = 0

for i in range(n):
   for j in range(m):
       #dfs 실행 후 True를 받아오면
       if dfs(i,j) == True:
           result += 1
print(result)