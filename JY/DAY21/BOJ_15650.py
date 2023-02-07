import sys

input = sys.stdin.readline

total, n = map(int, input().split())
res = []
store = []
def dfs():
    cnt = 0
    if len(res) == n:
        for k in range(len(store)):
            for j in range(total):
                if k[j] in res:
                    cnt += 1
            if cnt == total:
                break
        if cnt == total:
            store.append(res)
            print(" ".join(map(str, res)))
    for i in range(1, total+1):
        if i not in res:
            res.append(i)
            dfs()
            res.pop()