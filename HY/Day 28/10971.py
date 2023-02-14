import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split()))for _ in range(n)]
answer = sys.maxsize
visited = [False] * n

def dfs(start, now, value, cnt):
    global answer
    if cnt == n:
        if a[now][start]: #지금~시작점
            value += a[now][start]
            if answer > value:
                answer = value
        return

    if value > answer:
        return

    for i in range(n):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(answer)