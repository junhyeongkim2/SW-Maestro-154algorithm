# 9466번 텀 프로젝트
# https://www.acmicpc.net/problem/9466

import sys
from collections import deque

read = sys.stdin.readline

for _ in range(int(read())):
    N = int(read())
    stud = list(map(int, ('0 ' + read()).split()))
    visit = [0 for _ in range(N + 1)]

    cnt = 0
    for i in range(1, N + 1):  # 1~N
        if visit[i]:  # 이전에 방문한 경우
            continue
        que = deque()
        que.append(i)
        pick = list()
        visit[i] = 1
        while True:
            x = stud[que[-1]]  # i가 가리키는 번호
            if not visit[x]:  # 방문하지 않은 경우
                que.append(x)
                visit[x] = 1
            else:  # 방문한 경우
                for c in que:
                    if c == x:
                        break
                    cnt += 1
                break

    print(cnt)