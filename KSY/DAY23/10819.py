N = int(input())
alist = list(map(int, input().split()))

answer = 0
visited = [False]*N


def backtracking(candidate):
    global answer
    if len(candidate) == N:
        temp = 0
        for i in range(len(candidate)-1):
            temp += abs(candidate[i] - candidate[i+1])
        answer = max(temp, answer)

    for i in range(len(alist)):  # 각 자리에 가능한 모든 수 뽑기
        if not visited[i]:  # 뽑지 않은 수 일 경우
            candidate.append(alist[i])
            visited[i] = True  # 방문 표시
            backtracking(candidate)

            candidate.pop()  # 특정 숫자 선택 후 다른 숫자를 해당 자리에 위치 시키기 위해 다시 돌려 놓는다
            visited[i] = False

backtracking([])
print(answer)
