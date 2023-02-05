import sys
from collections import deque


input = sys.stdin.readline

A, B = map(int, input().split())
MAX = 10**5
dist = [0] * (MAX + 1)

def bfs():
    qu = deque()
    qu.append(A)
    while qu:
        x = qu.popleft()
        if x == B:
            print(dist[x])
            break
        for nx in (x -1, x + 1, x*2):
            if 0 <= nx <= MAX and not dist[nx]: # and 기준으로 조건 순서를 바꾸면 안된다. 
                dist[nx] = dist[x] + 1
                qu.append(nx)
bfs()