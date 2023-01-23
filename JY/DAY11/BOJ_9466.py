import sys
#sys.setrecursionlimit(5000) -> 런타임에러 
sys.setrecursionlimit(111111)

def dfs(start):
    global res
    visited[start] = True
    cir.append(start)
    next = int(st[start])
    if visited[next] == True:
        if next in cir:
            res += cir[cir.index(next):]
        return
    else:
        dfs(next)
        
            
for _ in range(int(sys.stdin.readline())):
    res =[]
    total = int(input())
    st = [0] + list(sys.stdin.readline().split())
    visited = [False] * (total+1)
    for i in range(1, total+1):
        if visited[i] == False:
            cir = []
            dfs(i)
    print((total - len(res)))
    