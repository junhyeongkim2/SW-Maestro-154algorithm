import sys
N = int(input())

cities = []
visited = [False] * N  # 방문한 도시 확인
answer = sys.maxsize  # 가장 작은 결과를 담을 변수
for i in range(N):
    cities.append(list(map(int, input().split())))


def tsp(start, next, sum):
    global answer
    if visited.count(True) == N:  # 도시를 모두 방문 했을 때
        if cities[next][start]:  # 마지막 도시에서 처음 도시로 갈 수 있을 때
            answer = min(answer, sum + cities[next][start])

    for i, c in enumerate(cities[next]):  # next에서 갈 수 있는 모든 도시
        if c != 0 and not visited[i] and answer > sum:  # 방문 하지 않은, 본인이 아닌, 갈 수 있는, **앞으로 더 작아질 수 있는
            visited[i] = True
            tsp(start, i, sum + cities[next][i])
            visited[i] = False


for i in range(N):  # 시작 도시 선택
    visited[i] = True
    tsp(i, i, 0)
    visited[i] = False

print(answer)
