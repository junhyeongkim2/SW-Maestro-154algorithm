n = int(input())
a = list(map(int, input().split()))
t = []
visit = [0] * n
ans = 0
def dfs(depth):
    global n, ans
    if depth == n:
        total = 0
        for i in range(1, n):
            total += abs(t[i-1] - t[i])
        ans = max(ans, total)
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            t.append(a[i])
            dfs(depth + 1)
            visit[i] = 0
            t.pop()
dfs(0)
print(ans)