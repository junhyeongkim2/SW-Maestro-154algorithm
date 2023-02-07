import sys
input = sys.stdin.readline
testcase = int(input())

for _ in range(testcase):
    next, result = 0, 0
    N = int(input())
    visited = set()
    permutation = list(map(int, input().split()))
    permutation = [(i+1, n) for i, n in enumerate(permutation)]

    for i in range(N):
        if permutation[i][0] not in visited:
            visited.add(permutation[i][0])
            next = permutation[i][1]
            while next != permutation[i][0]: #본인으로 돌아올 때까지 반복
                visited.add(next)
                next = permutation[next-1][1]
            if next == permutation[i][0]:
                result += 1
    print(result)

