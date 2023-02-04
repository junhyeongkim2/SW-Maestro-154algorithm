import sys

input = sys.stdin.readline

total, n = map(int, input().split())
res = []

def dfs():
    if len(res) == n:
        print(' '.join(map(str,res)))
        return 
    for k in range(1, total+1):
        if k not in res:
            res.append(k)
            dfs()
            res.pop()
    
dfs()
