import sys
import math
from collections import deque
input = sys.stdin.readline


total = int(input())
li = []

num = 100000
arr = [True] * (num+1)

for k in range(2, int(math.sqrt(num))+1):
    if arr[k] == True:
        j = 2
        while k * j <= num:
            arr[k*j] = False
            j += 1

def bfs(start, end):
    qu = deque()
    qu.append([start, 0])
    visited = [False] * (num+1)
    visited[start] = True
    while qu:
        x , cnt = qu.popleft()
        xs= str(x)
        if x == end:
            return cnt
        for i in range(4):
            for j in range(10):
                tmp = int(str(xs[:i]) + str(j) + str(xs[i+1:]))
                if not visited[tmp] and arr[tmp]and 1000 <= tmp:
                    qu.append([tmp, cnt+1])
                    visited[tmp] = True
            
        
for _ in range(total):
    start, end = map(int, input().split())
    result = bfs(start, end)
    print(result if result != None else "Impossible")