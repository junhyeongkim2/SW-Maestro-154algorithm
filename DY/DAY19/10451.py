# 10451번 순열 사이클
# https://www.acmicpc.net/problem/10451
import sys
read = sys.stdin.readline

T = int(read().strip())
for _ in range(T):
    N = int(read().strip())
    graph = [0] + list(map(int, read().split()))
    visit = [False] * (N + 1)
    cnt = 0
    for node in range(1, N + 1):
        if visit[node]: continue  # 이미 방문한 경우
        cnt += 1
        visit[node] = True
        next = graph[node]
        while not visit[next]:
            visit[next] = True
            next = graph[next]
    print(cnt)