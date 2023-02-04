"""
문제 : 공유기 N개를 설치하면 집 사이에 거리가 최대는 몇일까

(1) 공유기 설치 위치
중간값보다 커야 설치가 가능하다.
처음 거리보다 다음 설치한 공유기의 거리가 더 넓게 거리를 잡아간다
(마지막 설치 집 -설치예정 집) > mid
다 설치를 했는데 C보다 작으면 공유기 간격을 좁힌다
공유기 개수가 C보다 크면 공유기 간격을 넓힌다.
"""
import sys
input = sys.stdin.readline
N, C = map(int, input().split())
home = []

for _ in range(N):
    home.append(int(input()))

home.sort()

start, end = 1, (home[-1]-home[0])  # 시작점, 끝점
answer = 0

while start <= end:
    mid = (start + end) // 2
    sum = 1
    cur = home[0] #현재 집의 위치 

    #두번째 집부터 탐색
    for i in range(N):
        if home[i] - cur >= mid:    #설치예정인 집이 마지막으로 설치한 곳과의 거리보다 크면 설치
            sum += 1
            cur = home[i] #마지막 설치위치 기록
    #만약 총 설치값이 C보다 크면 
    if sum >= C:
        answer = mid #일단 기록 
        start = mid + 1 #간격을 줄인다
    else: #총 설치값이 C보다 작으면
        end = mid - 1 #간격을 늘린다

print(answer)