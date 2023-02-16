import sys

input = sys.stdin.readline

sys.setrecursionlimit(5000)


def dfs(start):
    v[start] = True
    for i in arr[start]:
        if v[i] == False:
            dfs(i)


n, m = map(int, input().split())
arr = [[] for i in range(n + 1)]

for i in range(m):
    n1, n2 = map(int, input().split())
    arr[n1].append(n2)
    arr[n2].append(n1)

v = [False] * (n + 1)
cnt = 0

for i in range(1, n + 1):
    if v[i] == False:
        if not arr[i]:
            cnt += 1
            v[i] = True
        else:
            dfs(i)
            cnt += 1


print(cnt)
