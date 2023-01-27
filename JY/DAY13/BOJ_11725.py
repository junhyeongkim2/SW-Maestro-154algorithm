import sys
from collections import deque
input = sys.stdin.readline
total = int(input())
tree = [[] for _ in range(total+1)]
parent = [0] * (total + 1)
visited = [False] * (total + 1)

for _ in range(total-1):
    a, b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def bfs(start):
    qu = deque([start])
    visited[start] = True 
    while qu:
        v = qu.popleft()
        for k in tree[v]:
            if not visited[k]:
                visited[k] = True
                parent[k] = v
                qu.append(k)
        
        
bfs(1)
for i in range(2,total+1):
        print(parent[i])

    


 