from itertools import combinations

def dfs(cur):
    if len(result)==L:
        v = len(set(result)&{'a','e','i','o','u'})
        if L-v<2 or v==0:
            return -1
        print(''.join(result))

    for i in range(cur+1, C):
        if arr[i] not in result:
            result.append(arr[i])
            dfs(i)
            result.pop()

L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
result = []

dfs(-1)