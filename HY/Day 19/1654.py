import sys
input = sys.stdin.readline

K, Need = map(int, input().split())
lines = []

for i in range(K):
    lines.append(int(input()))

start, end = 1, max(lines)  # 시작점, 끝점

while start <= end:
    mid = (start + end) // 2  # 중간점
    sum = 0
    for i in lines:
        sum += i // mid  # 자른 랜선의 합

# 이진탐색 알고리즘
    if sum >= Need:      # sum이 Need보다 크면 (원하는 것보다 합이 더 많으면)
        start = mid + 1  # start를 늘려서  더 크게 잘라 sum을 줄임
    else:                # sum이 Need보다 작으면 (원하는 것보다 합이 더 적으면)
        end = mid - 1    # end를 줄여서 작게 잘라서 수를 늘림

print(end)
