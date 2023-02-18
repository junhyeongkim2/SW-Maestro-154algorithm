def solution(N, S):
    alist = list(map(int, input().split()))

    currentSum = 0
    result = 0

    def dfs(level):
        nonlocal currentSum
        nonlocal result
        if level != N:  # 더이상 내려갈 곳이 없는 상태
            if alist[level] + currentSum == S:  # 해당 위치의 값을 더한 것이 원하는 값일 때
                result += 1

            dfs(level + 1)  # 더하지 않고 다음 단계
            currentSum += alist[level]
            dfs(level + 1)  # 더하고 다음 단계
            currentSum -= alist[level]  # (중요) 더했던 값 빼기

    dfs(0)
    return result

N, S = map(int, input().split())
print(solution(N, S))
