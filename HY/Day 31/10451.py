"""
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 
각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다. 
둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.
순열 사이클을 출력해라
"""
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
        if not visited[i]:
            dfs(i)
            answer += 1
    print(answer)