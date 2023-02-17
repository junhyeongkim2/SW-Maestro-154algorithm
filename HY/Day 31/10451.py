import sys
input = sys.stdin.readline
sys.setrecursionlimit(10*7)

t = int(input())

def dfs(v):
    visited[v] = True
    next = arr[v]
    if visited[next] == False:
        dfs(next)

    # 테스트 케이스 t만큼 실행
for _ in range(t):
    answer = 0
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n  + 1)

    # 순열 개수 세기
    for i in range(1, n+1):
        if not visited [i]:
            dfs(i)
            answer += 1
    print(answer)