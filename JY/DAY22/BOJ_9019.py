import sys
from collections import deque

input = sys.stdin.readline

total = int(input())
visited= [False] * (10000+1)
res = []
li = [x*2, x-1, (x - (int(t[0])//(10**(len(t)-1))))*10 + int(t[0])),(x-int(t[-1])//10 + int(t[-1])*(10**(len(t)-1))]
def bfs(start, end):
    qu = deque()
    qu.append(start)
    visited[start] = True
    while qu:
        x = qu.popleft()
        if x == end:
            return res
        t = str(x)
        cnt = 0
        for k in li:
            if k > 9999:
                k = k %10000
            qu.append(k)
            if cnt == 0:
                res.append("D")
            elif cnt == 1:
                res.append("S")
            elif cnt == 2:
                res.append("L")
            elif cnt == 3:
                res.append("R")
            cnt += 1

for _ in range(total):
    A, B = map(int, input().split())
    print("".join(bfs(A, B)))