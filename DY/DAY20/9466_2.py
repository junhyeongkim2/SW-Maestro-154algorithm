# 9466번 텀 프로젝트
# https://www.acmicpc.net/problem/9466
import sys
read = sys.stdin.readline

T = int(read().strip())
for _ in range(T):
    n = int(read().strip())
    graph = [0]+list(map(int, read().split()))
    visit = {}
    result = 0
    cnt = 1
    for i in range(1, n+1):
        try:
            if visit[i]: # 앞에서 방문한 경우
                continue
        except:
            visit[i] = cnt
            cnt += 1
        node = i
        while True:
            node = graph[node] # i가 가리키는 노드
            try:
                if visit[node]: # 이미 앞에서 나온 경우
                    if visit[i] <= visit[node]:
                        result += cnt - visit[node]
                    else:
                        break
                    break
            except: # 앞에서 나오지 않은 경우
                visit[node] = cnt
                cnt += 1
    print(n-result)
